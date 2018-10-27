import uuid
from djoser.views import UserView, UserDeleteView
from djoser import serializers
from rest_framework import views, permissions, status, permissions, generics, filters
from rest_framework.response import Response
from . import models
from . import serializers
from .serializers import IdeaSerializer
from rest_framework.decorators import api_view

class IdeaView(generics.ListCreateAPIView):
    """Use this endpoint to add ideas in the backend."""
    def get_queryset(self):
        queryset = models.Idea.objects.all()
        idea_id = self.request.query_params.get('id', None)
        idea_cursor = self.request.query_params.get('idea_cursor', None)

        if idea_id is None:
            if idea_cursor is None:
                return queryset
            else:
                return queryset[int(idea_cursor):int(idea_cursor)+5]
        else:
            return queryset.filter(id=idea_id)

    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.IdeaSerializer

@api_view(['PUT'])
def update_upvotes(request, idea_id):
    idea = models.Idea.objects.get(pk = idea_id)
    user = models.User.objects.get(pk = request.user.id)
    is_idea_upvoted = user.upvoted_ideas.filter(idea_id=idea_id)
    upvotes = idea.upvotes

    if is_idea_upvoted:
        upvotes -= 1
        user.upvoted_ideas.filter(idea_id=idea_id).delete()
    else:
        upvotes += 1
        user.upvoted_ideas.create(idea=idea, user=user)   
    serializer = serializers.IdeaSerializer(idea, data = {'upvotes': upvotes}, partial = True)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST) 


class UserUpvotedIdeasView(generics.ListCreateAPIView):
    """Use this endpoint to fetch upvoted ideas from the backend."""

    def get_queryset(self):
        queryset = models.Upvoted_ideas.objects.all()
        return queryset
    model = models.Upvoted_ideas
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserUpvotedIdeasSerializer
