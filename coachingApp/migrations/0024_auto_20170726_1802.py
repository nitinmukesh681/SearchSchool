# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0023_likesarticles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likesarticles',
            name='liked_by',
        ),
        migrations.RemoveField(
            model_name='likesarticles',
            name='likes_object',
        ),
        migrations.RemoveField(
            model_name='likesarticles',
            name='object_topic',
        ),
        migrations.DeleteModel(
            name='likesArticles',
        ),
    ]
