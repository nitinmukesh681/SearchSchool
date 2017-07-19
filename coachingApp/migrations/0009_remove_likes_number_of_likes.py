# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0008_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='number_of_likes',
        ),
    ]
