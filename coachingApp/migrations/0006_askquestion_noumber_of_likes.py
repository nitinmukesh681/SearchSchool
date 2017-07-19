# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0005_aboutinstitution_addedby'),
    ]

    operations = [
        migrations.AddField(
            model_name='askquestion',
            name='noumber_of_likes',
            field=models.BigIntegerField(default=0, blank=True, null=True),
        ),
    ]
