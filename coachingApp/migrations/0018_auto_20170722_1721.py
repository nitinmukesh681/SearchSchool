# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0017_help_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askquestion',
            name='answer_on_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='askquestion',
            name='answer_on_time',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
