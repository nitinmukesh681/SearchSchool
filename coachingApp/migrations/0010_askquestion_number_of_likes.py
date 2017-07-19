# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0009_remove_likes_number_of_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='askquestion',
            name='number_of_likes',
            field=models.BigIntegerField(default=0, null=True, blank=True),
        ),
    ]
