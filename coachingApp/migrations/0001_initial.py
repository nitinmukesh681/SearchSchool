# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutInstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('Institution_name', models.CharField(null=True, blank=True, max_length=100)),
                ('InstitutionCategory', models.CharField(null=True, blank=True, max_length=100, choices=[('Coaching', 'Coaching'), ('School', 'School'), ('College', 'College')])),
                ('InstitutionType', models.CharField(null=True, blank=True, max_length=100, choices=[('Government', 'Government'), ('Private', 'Private'), ('Trust', 'Trust')])),
                ('established_year', models.DateField(null=True, blank=True)),
                ('contact_details', models.BigIntegerField(null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('email', models.EmailField(null=True, blank=True, max_length=254)),
                ('person_to_contact', models.CharField(null=True, blank=True, max_length=350)),
                ('full_address', models.CharField(null=True, blank=True, max_length=300)),
                ('pincode', models.IntegerField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AskQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('asked_Date', models.DateField(null=True, auto_now_add=True)),
                ('asked_Time', models.TimeField(null=True, auto_now_add=True)),
                ('Asked_Question', models.TextField(null=True, blank=True)),
                ('answer_is', models.TextField(null=True, blank=True)),
                ('is_answered_YesNo', models.BooleanField(default=False)),
                ('answer_on_date', models.DateField(null=True, auto_now_add=True)),
                ('answer_on_time', models.TimeField(null=True, auto_now_add=True)),
                ('is_edited_YesNo', models.BooleanField(default=False)),
                ('edited_on_date', models.DateField(null=True, auto_now_add=True)),
                ('edited_on_time', models.TimeField(null=True, auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CityMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(null=True, blank=True, max_length=100)),
                ('last_modifiedBy', models.CharField(null=True, blank=True, max_length=100)),
                ('last_modified_DateTime', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CountryMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(null=True, blank=True, max_length=100)),
                ('last_modifiedBy', models.CharField(null=True, blank=True, max_length=100)),
                ('last_modified_DateTime', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('gender', models.CharField(null=True, blank=True, max_length=300)),
                ('image', models.ImageField(upload_to='profile_image', blank=True)),
                ('mobileNumber', models.BigIntegerField(null=True, blank=True)),
                ('full_address', models.CharField(null=True, blank=True, max_length=300)),
                ('pincode', models.IntegerField(null=True, blank=True)),
                ('isProfileComplete', models.BooleanField(default=False)),
                ('is_activeYesNO', models.BooleanField(default=False)),
                ('is_loggedIn', models.BooleanField(default=False)),
                ('last_logged_in', models.DateTimeField(null=True, blank=True)),
                ('Number_of_reviews', models.IntegerField(default=0)),
                ('created_date_time', models.DateTimeField(null=True, blank=True)),
                ('city', models.ForeignKey(to='coachingApp.CityMaster', blank=True, null=True)),
                ('country', models.ForeignKey(to='coachingApp.CountryMaster', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResultCategoryMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(null=True, blank=True, max_length=200)),
                ('addedDateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewAboutInstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('review_title', models.CharField(null=True, blank=True, max_length=650)),
                ('review', models.CharField(null=True, blank=True, max_length=650)),
                ('addedDateTime', models.DateField(null=True, blank=True)),
                ('InstitutionName', models.ForeignKey(to='coachingApp.AboutInstitution', blank=True, null=True)),
                ('addedBy', models.ForeignKey(to='coachingApp.MyUser', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(null=True, blank=True, max_length=100)),
                ('last_modifiedBy', models.CharField(null=True, blank=True, max_length=100)),
                ('last_modified_DateTime', models.DateTimeField(null=True, blank=True)),
                ('countryId', models.ForeignKey(to='coachingApp.CountryMaster', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='statistical_data_institution',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('result_year', models.DateField(null=True, blank=True)),
                ('no_of_student_admitted', models.BigIntegerField(null=True, blank=True)),
                ('no_of_student_succed', models.BigIntegerField(null=True, blank=True)),
                ('InstitutionName', models.ForeignKey(to='coachingApp.AboutInstitution', blank=True, null=True)),
                ('result_name', models.ForeignKey(to='coachingApp.ResultCategoryMaster', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TopicMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(null=True, blank=True, max_length=200)),
                ('addedDateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='state',
            field=models.ForeignKey(to='coachingApp.StateMaster', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='citymaster',
            name='stateId',
            field=models.ForeignKey(to='coachingApp.StateMaster', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='askquestion',
            name='Ask_topic',
            field=models.ForeignKey(to='coachingApp.TopicMaster', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='askquestion',
            name='Asked_to',
            field=models.ForeignKey(to='coachingApp.MyUser', related_name='asked_to', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='askquestion',
            name='userAsked',
            field=models.ForeignKey(to='coachingApp.MyUser', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutinstitution',
            name='city',
            field=models.ForeignKey(to='coachingApp.CityMaster', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutinstitution',
            name='country',
            field=models.ForeignKey(to='coachingApp.CountryMaster', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutinstitution',
            name='state',
            field=models.ForeignKey(to='coachingApp.StateMaster', blank=True, null=True),
        ),
    ]
