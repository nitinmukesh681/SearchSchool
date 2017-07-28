# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0024_auto_20170726_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutinstitution',
            name='established_year',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
