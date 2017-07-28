# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0025_auto_20170728_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutinstitution',
            name='established_year',
            field=models.IntegerField(null=True, default=0, blank=True),
        ),
    ]
