# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0002_auto_20170729_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askquestion',
            name='asked_Date',
            field=models.DateField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='askquestion',
            name='asked_Time',
            field=models.TimeField(null=True, auto_now_add=True),
        ),
    ]
