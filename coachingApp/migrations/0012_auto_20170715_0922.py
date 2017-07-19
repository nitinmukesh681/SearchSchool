# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0011_auto_20170715_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='liked_by',
            field=models.ForeignKey(null=True, blank=True, to='coachingApp.MyUser'),
        ),
    ]
