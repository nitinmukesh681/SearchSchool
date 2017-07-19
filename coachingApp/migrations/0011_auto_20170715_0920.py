# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0010_askquestion_number_of_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='likes_object',
            field=models.ForeignKey(blank=True, to='coachingApp.AskQuestion', null=True),
        ),
        migrations.AddField(
            model_name='likes',
            name='object_topic',
            field=models.ForeignKey(blank=True, to='coachingApp.TopicMaster', null=True),
        ),
    ]
