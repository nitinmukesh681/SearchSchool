# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0016_auto_20170720_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help_Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('subject', models.CharField(max_length=150, null=True, blank=True)),
                ('message', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
