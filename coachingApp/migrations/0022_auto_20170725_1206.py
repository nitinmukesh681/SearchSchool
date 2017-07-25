# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0021_yourarticle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutinstitution',
            name='InstitutionType',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
