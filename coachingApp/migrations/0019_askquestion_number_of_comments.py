# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0018_auto_20170722_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='askquestion',
            name='number_of_comments',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]
