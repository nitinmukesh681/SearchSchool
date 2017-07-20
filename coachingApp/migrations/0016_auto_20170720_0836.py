# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coachingApp', '0015_auto_20170720_0832'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
                ('uploaded_date_time', models.DateTimeField(null=True, auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutinstitution',
            name='image',
        ),
        migrations.RemoveField(
            model_name='aboutinstitution',
            name='uploaded_date_time',
        ),
        migrations.AddField(
            model_name='institutionimage',
            name='InstitutionName',
            field=models.ForeignKey(to='coachingApp.AboutInstitution', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='institutionimage',
            name='userId',
            field=models.OneToOneField(to='coachingApp.MyUser', null=True, blank=True),
        ),
    ]
