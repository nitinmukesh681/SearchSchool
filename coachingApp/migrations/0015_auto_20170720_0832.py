# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0014_auto_20170718_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institutionimage',
            name='InstitutionName',
        ),
        migrations.RemoveField(
            model_name='institutionimage',
            name='userId',
        ),
        migrations.AddField(
            model_name='aboutinstitution',
            name='image',
            field=models.ImageField(upload_to='profile_image', blank=True),
        ),
        migrations.AddField(
            model_name='aboutinstitution',
            name='uploaded_date_time',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='InstitutionImage',
        ),
    ]
