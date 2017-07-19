# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0003_auto_20170713_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='uploaded_date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='userId',
            field=models.OneToOneField(blank=True, to='coachingApp.MyUser', null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='image_url',
            field=models.CharField(max_length=500, blank=True, null=True),
        ),
    ]
