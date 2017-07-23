# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0020_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourArticle',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('article_heading', models.CharField(max_length=300, null=True, blank=True)),
                ('article_is', models.TextField(null=True, blank=True)),
                ('article_about', models.CharField(max_length=300, null=True, blank=True)),
                ('article_date', models.DateField(null=True, blank=True)),
                ('article_time', models.TimeField(null=True, blank=True)),
                ('number_of_likes', models.BigIntegerField(null=True, blank=True, default=0)),
                ('number_of_comments', models.BigIntegerField(null=True, blank=True, default=0)),
                ('addedBy', models.ForeignKey(null=True, blank=True, to='coachingApp.MyUser')),
            ],
        ),
    ]
