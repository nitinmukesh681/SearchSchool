# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0029_auto_20170728_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutinstitution',
            name='established_year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
