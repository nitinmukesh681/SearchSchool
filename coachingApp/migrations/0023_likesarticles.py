# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0022_auto_20170725_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='likesArticles',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('like_type', models.CharField(blank=True, max_length=200, choices=[('Topics', 'Topics'), ('Comment', 'Comment'), ('Answer', 'Answer')], null=True)),
                ('liked_date_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('liked_by', models.ForeignKey(blank=True, null=True, to='coachingApp.MyUser')),
                ('likes_object', models.ForeignKey(blank=True, null=True, to='coachingApp.YourArticle')),
                ('object_topic', models.ForeignKey(blank=True, null=True, to='coachingApp.TopicMaster')),
            ],
        ),
    ]
