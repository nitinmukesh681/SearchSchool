# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0006_askquestion_noumber_of_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='askquestion',
            name='noumber_of_likes',
        ),
    ]
