# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0019_askquestion_number_of_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('comment_Content', models.TextField(blank=True, null=True)),
                ('comment_date', models.DateField(blank=True, null=True)),
                ('comment_time', models.TimeField(blank=True, null=True)),
                ('Question_is', models.ForeignKey(blank=True, null=True, to='coachingApp.AskQuestion')),
                ('comment_by', models.ForeignKey(blank=True, null=True, to='coachingApp.MyUser')),
            ],
        ),
    ]
