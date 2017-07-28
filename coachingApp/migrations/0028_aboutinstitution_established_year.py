# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0027_remove_aboutinstitution_established_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutinstitution',
            name='established_year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
