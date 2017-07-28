# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0026_auto_20170728_0826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutinstitution',
            name='established_year',
        ),
    ]
