# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0013_auto_20170718_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
                ('uploaded_date_time', models.DateTimeField(null=True, auto_now_add=True)),
                ('InstitutionName', models.ForeignKey(null=True, to='coachingApp.AboutInstitution', blank=True)),
                ('userId', models.OneToOneField(null=True, to='coachingApp.MyUser', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='document',
            name='InstitutionName',
        ),
    ]
