# Generated by Django 2.0.7 on 2018-10-08 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0017_auto_20181008_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 8, 13, 38, 45, 871530)),
        ),
        migrations.AlterField(
            model_name='idea',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 8, 13, 38, 45, 870945)),
        ),
    ]