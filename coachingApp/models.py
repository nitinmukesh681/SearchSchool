from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.


class CountryMaster(models.Model):
	name = models.CharField(max_length = 100,null = True,blank = True)
	last_modifiedBy = models.CharField(max_length = 100,null = True, blank = True)
	last_modified_DateTime = models.DateTimeField(null = True,blank = True)

	def __str__(self):
		return '%s' % (self.name)

class StateMaster(models.Model):
	name = models.CharField(max_length = 100,null = True,blank = True)
	countryId = models.ForeignKey(CountryMaster,null = True,blank = True)
	last_modifiedBy = models.CharField(max_length = 100,null = True, blank = True)
	last_modified_DateTime = models.DateTimeField(null = True,blank = True)

	def __str__(self):
		return '%s' % (self.name)

class CityMaster(models.Model):
	name = models.CharField(max_length = 100,null = True,blank = True)
	stateId = models.ForeignKey(StateMaster,null = True,blank = True)
	last_modifiedBy = models.CharField(max_length = 100,null = True, blank = True)
	last_modified_DateTime = models.DateTimeField(null = True,blank = True)

	def __str__(self):
		return '%s' % (self.name)


class MyUser(models.Model):
	user = models.OneToOneField(User,null = True, blank = True)
	gender = models.CharField(max_length = 300,null = True, blank = True)
	country = models.ForeignKey(CountryMaster,null = True,blank = True)
	state = models.ForeignKey(StateMaster,null = True,blank = True)
	city = models.ForeignKey(CityMaster,null = True,blank = True)
	image_url = models.CharField(max_length = 500, null = True, blank = True)
	is_image_uploaded = models.BooleanField(default = False)
	mobileNumber = models.BigIntegerField(null = True, blank = True)
	full_address = models.CharField(max_length = 300,null = True, blank = True)
	pincode = models.IntegerField(null = True,blank = True)
	isProfileComplete = models.BooleanField(default = False)
	is_activeYesNO = models.BooleanField(default = False)
	is_loggedIn = models.BooleanField(default = False)
	last_logged_in = models.DateTimeField(null = True, blank = True)
	Number_of_reviews = models.IntegerField(default = 0)
	created_date_time = models.DateTimeField(null = True, blank = True)
	def __str__(self):
		return '%s %s' % (self.user.username,self.mobileNumber)

class Document(models.Model):
	userId = models.OneToOneField(MyUser,null = True,blank = True)
	image = models.ImageField(upload_to = 'profile_image',blank = True)	
	uploaded_date_time = models.DateTimeField(auto_now_add = True,null = True,blank = True)
	def __str__(self):
		return '%s' % (self.id)


class AboutInstitution(models.Model):
	mm = (('Coaching','Coaching'),('School','School'),('College','College'))
	mms = (('Government','Government'),('Private','Private'),('Trust','Trust'))
	addedBy = models.ForeignKey(MyUser,null = True, blank = True)
	Institution_name = models.CharField(max_length = 100,null = True, blank = True)
	InstitutionCategory = models.CharField(max_length = 100,choices = mm, null = True, blank = True)
	InstitutionType = models.CharField(max_length = 100,choices = mms, null = True, blank = True)	
	established_year = models.DateField(null = True, blank = True)
	contact_details = models.BigIntegerField(null = True,blank = True)
	website = models.URLField(null = True,blank = True,max_length = 200)
	email = models.EmailField(null = True,blank = True)
	person_to_contact = models.CharField(max_length = 350, null = True,blank = True)
	country = models.ForeignKey(CountryMaster,null = True,blank = True)
	state = models.ForeignKey(StateMaster,null = True,blank = True)
	city = models.ForeignKey(CityMaster,null = True,blank = True)
	full_address = models.CharField(max_length = 300,null = True, blank = True)
	pincode = models.IntegerField(null = True,blank = True)
	description = models.TextField(null = True,blank = True)
	is_image_uploaded = models.BooleanField(default = False)
	# reviewStatus = models.ForeignKey(ReviewAboutInstitution,null = True,blank = True)
	def __str__(self):
		return '%s %s %s' % (self.id,self.Institution_name,self.website)


class ReviewAboutInstitution(models.Model):
	InstitutionName = models.ForeignKey(AboutInstitution,null = True,blank = True)
	review_title = models.CharField(max_length = 650,null = True,blank =True)
	review = models.CharField(max_length = 650,null = True,blank =True)
	addedBy = models.ForeignKey(MyUser,null = True,blank = True)
	addedDateTime = models.DateField(null = True,blank = True)
	
	def __str__(self):
		return '%s %s %s' % (self.id,self.InstitutionName.Institution_name,self.InstitutionName.website)

class TopicMaster(models.Model):
	name = models.CharField(max_length = 200, null = True, blank = True)
	addedDateTime = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return '%s' % (self.name)

class AskQuestion(models.Model):
	userAsked = models.ForeignKey(MyUser,null = True, blank = True)
	Asked_to = models.ForeignKey(MyUser,related_name = 'asked_to', null = True, blank = True)
	asked_Date = models.DateField(auto_now_add = True,null = True, blank = True)
	asked_Time = models.TimeField(auto_now_add = True,null = True, blank = True)
	Asked_Question = models.TextField(null = True, blank = True)
	Ask_topic = models.ForeignKey(TopicMaster,null = True, blank = True)
	answer_is = models.TextField(null = True, blank = True)
	is_answered_YesNo = models.BooleanField(default = False)
	answer_on_date = models.DateField(auto_now_add = True,null = True,blank = True)
	answer_on_time = models.TimeField(auto_now_add = True,null = True, blank = True)
	is_edited_YesNo = models.BooleanField(default = False)
	edited_on_date = models.DateField(auto_now_add = True,null = True,blank = True)
	edited_on_time = models.TimeField(auto_now_add = True,null = True, blank = True)
	number_of_likes = models.BigIntegerField(default = 0, null = True, blank = True)

	def __str__(self):
		return 'Question is  %s and topic %s' % (self.Asked_Question,self.Ask_topic)

class likes(models.Model):
	mm = (('Topics','Topics'),('Comment','Comment'),('Answer','Answer'))
	liked_by = models.ForeignKey(MyUser,null = True,blank = True,on_delete=models.CASCADE)
	like_type = models.CharField(max_length = 200,null = True, blank = True, choices = mm)
	likes_object = models.ForeignKey(AskQuestion,null = True, blank = True)
	object_topic = models.ForeignKey(TopicMaster,null = True, blank = True)
	liked_date_time = models.DateTimeField(auto_now_add = True, blank = True, null = True)
	def __str__(self):
		return '%s %s' % (self.liked_by.user.username, self.liked_date_time)

class ResultCategoryMaster(models.Model):
	name = models.CharField(max_length = 200, null = True, blank = True)
	addedDateTime = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return '%s' % (self.name)


class statistical_data_institution(models.Model):
	
	InstitutionName = models.ForeignKey(AboutInstitution,null = True, blank = True)
	result_name = models.ForeignKey(ResultCategoryMaster, null = True, blank = True)
	result_year = models.DateField(null = True, blank = True)
	no_of_student_admitted = models.BigIntegerField(null = True, blank = True)
	no_of_student_succed = models.BigIntegerField(null = True, blank = True)

	def __str__(self):
		return '%s %s' % (self.id,self.InstitutionName)


class InstitutionImage(models.Model):
	userId = models.OneToOneField(MyUser,null = True,blank = True)
	InstitutionName = models.ForeignKey(AboutInstitution,null = True ,blank = True)
	image = models.ImageField(upload_to = 'profile_image',blank = True)	
	uploaded_date_time = models.DateTimeField(auto_now_add = True,null = True,blank = True)
	def __str__(self):
		return '%s' % (self.userId.user.username)
