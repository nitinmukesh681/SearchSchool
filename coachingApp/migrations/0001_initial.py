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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Institution_name', models.CharField(null=True, blank=True, max_length=100)),
                ('InstitutionCategory', models.CharField(choices=[('Coaching', 'Coaching'), ('School', 'School'), ('College', 'College')], null=True, blank=True, max_length=100)),
                ('InstitutionType', models.CharField(null=True, blank=True, max_length=100)),
                ('established_year', models.CharField(null=True, blank=True, max_length=6)),
                ('contact_details', models.BigIntegerField(null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('email', models.CharField(null=True, blank=True, max_length=300)),
                ('person_to_contact', models.CharField(null=True, blank=True, max_length=350)),
                ('full_address', models.CharField(null=True, blank=True, max_length=300)),
                ('pincode', models.IntegerField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('is_image_uploaded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AskQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asked_Date', models.DateField(auto_now_add=True, null=True)),
                ('asked_Time', models.TimeField(auto_now_add=True, null=True)),
                ('Asked_Question', models.TextField(null=True, blank=True)),
                ('answer_is', models.TextField(null=True, blank=True)),
                ('is_answered_YesNo', models.BooleanField(default=False)),
                ('answer_on_date', models.DateField(null=True, blank=True)),
                ('answer_on_time', models.TimeField(null=True, blank=True)),
                ('is_edited_YesNo', models.BooleanField(default=False)),
                ('edited_on_date', models.DateField(auto_now_add=True, null=True)),
                ('edited_on_time', models.TimeField(auto_now_add=True, null=True)),
                ('number_of_likes', models.BigIntegerField(default=0, null=True, blank=True)),
                ('number_of_comments', models.BigIntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CityMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, max_length=100)),
                ('last_modifiedBy', models.CharField(null=True, blank=True, max_length=100)),
                ('last_modified_DateTime', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_Content', models.TextField(null=True, blank=True)),
                ('comment_date', models.DateField(null=True, blank=True)),
                ('comment_time', models.TimeField(null=True, blank=True)),
                ('Question_is', models.ForeignKey(null=True, blank=True, to='coachingApp.AskQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='CountryMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, max_length=100)),
                ('last_modifiedBy', models.CharField(null=True, blank=True, max_length=100)),
                ('last_modified_DateTime', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile_image', blank=True)),
                ('uploaded_date_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Help_Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, max_length=150)),
                ('email', models.EmailField(null=True, blank=True, max_length=254)),
                ('subject', models.CharField(null=True, blank=True, max_length=150)),
                ('message', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile_image', blank=True)),
                ('uploaded_date_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('InstitutionName', models.ForeignKey(null=True, blank=True, to='coachingApp.AboutInstitution')),
            ],
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_type', models.CharField(choices=[('Topics', 'Topics'), ('Comment', 'Comment'), ('Answer', 'Answer')], null=True, blank=True, max_length=200)),
                ('liked_date_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(null=True, blank=True, max_length=300)),
                ('image_url', models.CharField(null=True, blank=True, max_length=500)),
                ('is_image_uploaded', models.BooleanField(default=False)),
                ('mobileNumber', models.BigIntegerField(null=True, blank=True)),
                ('full_address', models.CharField(null=True, blank=True, max_length=300)),
                ('pincode', models.IntegerField(null=True, blank=True)),
                ('isProfileComplete', models.BooleanField(default=False)),
                ('is_activeYesNO', models.BooleanField(default=False)),
                ('is_loggedIn', models.BooleanField(default=False)),
                ('last_logged_in', models.DateTimeField(null=True, blank=True)),
                ('Number_of_reviews', models.IntegerField(default=0)),
                ('created_date_time', models.DateTimeField(null=True, blank=True)),
                ('city', models.ForeignKey(null=True, blank=True, to='coachingApp.CityMaster')),
                ('country', models.ForeignKey(null=True, blank=True, to='coachingApp.CountryMaster')),
            ],
        ),
        migrations.CreateModel(
            name='ResultCategoryMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, max_length=200)),
                ('addedDateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewAboutInstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(null=True, blank=True, max_length=650)),
                ('review', models.CharField(null=True, blank=True, max_length=650)),
                ('addedDateTime', models.DateField(null=True, blank=True)),
                ('InstitutionName', models.ForeignKey(null=True, blank=True, to='coachingApp.AboutInstitution')),
                ('addedBy', models.ForeignKey(null=True, blank=True, to='coachingApp.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, max_length=100)),
                ('last_modifiedBy', models.CharField(null=True, blank=True, max_length=100)),
                ('last_modified_DateTime', models.DateTimeField(null=True, blank=True)),
                ('countryId', models.ForeignKey(null=True, blank=True, to='coachingApp.CountryMaster')),
            ],
        ),
        migrations.CreateModel(
            name='statistical_data_institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_year', models.DateField(null=True, blank=True)),
                ('no_of_student_admitted', models.BigIntegerField(null=True, blank=True)),
                ('no_of_student_succed', models.BigIntegerField(null=True, blank=True)),
                ('InstitutionName', models.ForeignKey(null=True, blank=True, to='coachingApp.AboutInstitution')),
                ('result_name', models.ForeignKey(null=True, blank=True, to='coachingApp.ResultCategoryMaster')),
            ],
        ),
        migrations.CreateModel(
            name='TopicMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, max_length=200)),
                ('addedDateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='YourArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_heading', models.CharField(null=True, blank=True, max_length=300)),
                ('article_is', models.TextField(null=True, blank=True)),
                ('article_about', models.CharField(null=True, blank=True, max_length=300)),
                ('article_date', models.DateField(null=True, blank=True)),
                ('article_time', models.TimeField(null=True, blank=True)),
                ('number_of_likes', models.BigIntegerField(default=0, null=True, blank=True)),
                ('number_of_comments', models.BigIntegerField(default=0, null=True, blank=True)),
                ('addedBy', models.ForeignKey(null=True, blank=True, to='coachingApp.MyUser')),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='state',
            field=models.ForeignKey(null=True, blank=True, to='coachingApp.StateMaster'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='likes',
            name='liked_by',
            field=models.ForeignKey(null=True, blank=True, to='coachingApp.MyUser'),
        ),
        migrations.AddField(
            model_name='likes',
            name='likes_object',
            field=models.ForeignKey(null=True, blank=True, to='coachingApp.AskQuestion'),
        ),
        migrations.AddField(
            model_name='likes',
            name='object_topic',
            field=models.ForeignKey(null=True, blank=True, to='coachingApp.TopicMaster'),
        ),
        migrations.AddField(
            model_name='institutionimage',
            name='userId',
            field=models.OneToOneField(null=True, blank=True, to='coachingApp.MyUser'),
        ),
        migrations.AddField(
            model_name='document',
            name='userId',
            field=models.OneToOneField(null=True, blank=True, to='coachingApp.MyUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_by',
            field=models.ForeignKey(null=True, blank=True, to='coachingApp.MyUser'),
        ),
        migrations.AddField(
            model_name='citymaster',
            name='stateId',
            field=models.ForeignKey(null=True, blank=True, to='coachingApp.StateMaster'),
        ),
        migrations.AddField(
            model_name='askquestion',
            name='Ask_topic',
            field=models.ForeignKey(null=True, blank=True, to='coachingApp.TopicMaster'),
        ),
        migrations.AddField(
            model_name='askquestion',
            name='Asked_to',
            field=models.ForeignKey(null=True, blank=True, to='coachingApp.MyUser', related_name='asked_to'),
        ),
        migrations.AddField(
            model_name='askquestion',
            name='userAsked',
            field=models.ForeignKey(null=True, blank=True, to='coachingApp.MyUser'),
        ),
        migrations.AddField(
            model_name='aboutinstitution',
            name='addedBy',
            field=models.ForeignKey(null=True, blank=True, to='coachingApp.MyUser'),
        ),
        migrations.AddField(
            model_name='aboutinstitution',
            name='city',
            field=models.ForeignKey(null=True, blank=True, to='coachingApp.CityMaster'),
        ),
        migrations.AddField(
            model_name='aboutinstitution',
            name='country',
            field=models.ForeignKey(null=True, blank=True, to='coachingApp.CountryMaster'),
        ),
        migrations.AddField(
            model_name='aboutinstitution',
            name='state',
            field=models.ForeignKey(null=True, blank=True, to='coachingApp.StateMaster'),
        ),
    ]
