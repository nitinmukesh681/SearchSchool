# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0004_aboutinstitution_school_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('comment_Content', models.TextField(blank=True, null=True)),
                ('comment_date', models.DateField(blank=True, null=True)),
                ('comment_time', models.TimeField(blank=True, null=True)),
                ('Article_is', models.ForeignKey(to='coachingApp.YourArticle', blank=True, null=True)),
                ('comment_by', models.ForeignKey(to='coachingApp.MyUser', blank=True, null=True)),
            ],
        ),
    ]
