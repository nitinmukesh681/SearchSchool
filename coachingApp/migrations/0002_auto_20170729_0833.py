# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askquestion',
            name='asked_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='askquestion',
            name='asked_Time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='askquestion',
            name='edited_on_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='askquestion',
            name='edited_on_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
