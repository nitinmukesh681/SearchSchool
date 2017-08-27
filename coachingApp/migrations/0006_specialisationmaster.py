# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0005_commentarticle'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialisationMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('addedOn', models.DateField(blank=True, null=True)),
                ('areaOfSpecialisation', models.ForeignKey(blank=True, null=True, to='coachingApp.TopicMaster')),
                ('userIs', models.ForeignKey(blank=True, null=True, to='coachingApp.MyUser')),
            ],
        ),
    ]
