# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0007_remove_askquestion_noumber_of_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('like_type', models.CharField(blank=True, null=True, choices=[('Topics', 'Topics'), ('Comment', 'Comment'), ('Answer', 'Answer')], max_length=200)),
                ('number_of_likes', models.BigIntegerField(blank=True, null=True, default=0)),
                ('liked_date_time', models.DateTimeField(null=True, auto_now_add=True)),
                ('liked_by', models.OneToOneField(blank=True, to='coachingApp.MyUser', null=True)),
            ],
        ),
    ]
