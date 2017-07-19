# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0004_auto_20170713_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutinstitution',
            name='addedBy',
            field=models.ForeignKey(blank=True, to='coachingApp.MyUser', null=True),
        ),
    ]
