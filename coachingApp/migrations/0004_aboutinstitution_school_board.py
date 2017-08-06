# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0003_auto_20170731_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutinstitution',
            name='school_board',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
