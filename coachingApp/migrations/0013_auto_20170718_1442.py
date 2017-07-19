# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0012_auto_20170715_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutinstitution',
            name='is_image_uploaded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='document',
            name='InstitutionName',
            field=models.ForeignKey(to='coachingApp.AboutInstitution', blank=True, null=True),
        ),
    ]
