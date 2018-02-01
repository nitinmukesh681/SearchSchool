from django.shortcuts import render,redirect,HttpResponse
import datetime
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from django.core.urlresolvers import reverse
from coachingApp.forms import DocumentForm


# Create your views here.
@csrf_exempt
def homepage(request):
	questionObject = AskQuestion.objects.latest('id')
	idS = questionObject.id
	questionObject1 = AskQuestion.objects.get(id = idS - 1)
	questionObject2= AskQuestion.objects.get(id = idS - 2)
	questionObject3 = AskQuestion.objects.get(id = idS - 3)
	questionObject4 = AskQuestion.objects.get(id = idS - 4)
	totalInstitution = AboutInstitution.objects.all().count()
	totalQuestion = AskQuestion.objects.all().count()
	totalComment = Comment.objects.all().count()
	return render(request,'index.html',{'totalComment':totalComment,'totalQuestion':totalQuestion,'totalInstitution':totalInstitution, 'questionObject':questionObject,'questionObject1':questionObject1,'questionObject2':questionObject2,'questionObject3':questionObject3,'questionObject4':questionObject4})

@csrf_exempt
def search(request):
	try:
		user = request.user
		myuserObject_o = MyUser.objects.get(user = user)
		into = True
		print(into)
		print('user is logged in')
		if request.method == 'POST':
			form = request.POST

			try:
				try:
					abcObject = form['search']
					InstitutionObject = AboutInstitution.objects.get(Institution_name = abcObject.capitalize())
					try:
						print(1)
						reviewObject = ReviewAboutInstitution.objects.filter(InstitutionName = InstitutionObject)
						return render(request,'info.html',{'user':user,'into':into,'reviewObject':reviewObject,'InstitutionObject':InstitutionObject})
					except:
						print(2)
						return render(request,'info.html',{'user':user,'into':into,'InstitutionObject':InstitutionObject})

				except:
					try:
						InstitutionObject = AboutInstitution.objects.get(website = form['search'])
						# return render(request,'info.html',{'InstitutionObject':InstitutionObject})

						try:
							print(3)
							reviewObject = ReviewAboutInstitution.objects.filter(InstitutionName = InstitutionObject)
							return render(request,'info.html',{'user':user,'into':into,'reviewObject':reviewObject,'InstitutionObject':InstitutionObject})
						except:
							print(4)
							return render(request,'info.html',{'user':user,'into':into,'InstitutionObject':InstitutionObject})


					except:
						try:
							print('city')
							xyzObject = form['search']
							cityObject = CityMaster.objects.get(name = xyzObject.capitalize())
							InstitutionObject = AboutInstitution.objects.filter(city = cityObject)
							return render(request,'info_1.html',{'user':user,'into':into,'InstitutionObject':InstitutionObject})
						except:
							try:
								InstitutionObject = AboutInstitution.objects.filter(pincode = form['search'])
								return render(request,'info_1.html',{'user':user,'into':into,'InstitutionObject':InstitutionObject})

							except:
								try:
									# user = request.user
									myuserObject = MyUser.objects.get(user = user)
									questionObject = AskQuestion.objects.latest('id')
									idS = questionObject.id
									questionObject1 = AskQuestion.objects.get(id = idS - 1)
									questionObject2= AskQuestion.objects.get(id = idS - 2)
									questionObject3 = AskQuestion.objects.get(id = idS - 3)
									questionObject4 = AskQuestion.objects.get(id = idS - 4)

									return render(request,'noResultLogin.html',{'myuserObject':myuserObject,'questionObject':questionObject,'questionObject1':questionObject1,'questionObject2':questionObject2,'questionObject3':questionObject3,'questionObject4':questionObject4})
								except:
									questionObject = AskQuestion.objects.latest('id')
									idS = questionObject.id
									questionObject1 = AskQuestion.objects.get(id = idS - 1)
									questionObject2= AskQuestion.objects.get(id = idS - 2)
									questionObject3 = AskQuestion.objects.get(id = idS - 3)
									questionObject4 = AskQuestion.objects.get(id = idS - 4)

									return render(request,'noResult.html',{'questionObject':questionObject,'questionObject1':questionObject1,'questionObject2':questionObject2,'questionObject3':questionObject3,'questionObject4':questionObject4})
								# return render(request,'noResult.html')

			except:
				try:
					user = request.user
					myuserObject = MyUser.objects.get(user = user)
					questionObject = AskQuestion.objects.latest('id')
					idS = questionObject.id
					questionObject1 = AskQuestion.objects.get(id = idS - 1)
					questionObject2= AskQuestion.objects.get(id = idS - 2)
					questionObject3 = AskQuestion.objects.get(id = idS - 3)
					questionObject4 = AskQuestion.objects.get(id = idS - 4)

					return render(request,'noResultLogin.html',{'myuserObject':myuserObject,'questionObject':questionObject,'questionObject1':questionObject1,'questionObject2':questionObject2,'questionObject3':questionObject3,'questionObject4':questionObject4})
				except:
					questionObject = AskQuestion.objects.latest('id')
					idS = questionObject.id
					questionObject1 = AskQuestion.objects.get(id = idS - 1)
					questionObject2= AskQuestion.objects.get(id = idS - 2)
					questionObject3 = AskQuestion.objects.get(id = idS - 3)
					questionObject4 = AskQuestion.objects.get(id = idS - 4)

					return render(request,'noResult.html',{'questionObject':questionObject,'questionObject1':questionObject1,'questionObject2':questionObject2,'questionObject3':questionObject3,'questionObject4':questionObject4})

		else:
			return redirect('/home/')


	except:

		into = False
		print(into)
		print('user is not logged in')
		if request.method == 'POST':
			form = request.POST

			try:
				try:
					abcObject = form['search']
					InstitutionObject = AboutInstitution.objects.get(Institution_name = abcObject.capitalize())
					try:
						reviewObject = ReviewAboutInstitution.objects.filter(InstitutionName = InstitutionObject)
						print('review found')
						return render(request,'info.html',{'into':into,'reviewObject':reviewObject,'InstitutionObject':InstitutionObject})
					except:
						try:
							print('review not found')
							imageObject = InstitutionImage.objects.filter(InstitutionName = InstitutionObject)
							return render(request,'info.html',{'imageObject':imageObject,'into':into,'InstitutionObject':InstitutionObject})
						except:
							return render(request,'info.html',{'into':into,'InstitutionObject':InstitutionObject})


				except:
					try:
						InstitutionObject = AboutInstitution.objects.get(website = form['search'])
						# return render(request,'info.html',{'InstitutionObject':InstitutionObject})

						try:
							print(3)
							reviewObject = ReviewAboutInstitution.objects.filter(InstitutionName = InstitutionObject)
							return render(request,'info.html',{'into':into,'reviewObject':reviewObject,'InstitutionObject':InstitutionObject})
						except:
							print(4)
							return render(request,'info.html',{'into':into,'InstitutionObject':InstitutionObject})


					except:
						try:
							xyzObject = form['search']
							cityObject = CityMaster.objects.get(name = xyzObject.capitalize())
							InstitutionObject = AboutInstitution.objects.filter(city = cityObject)
							return render(request,'info_1.html',{'into':into,'InstitutionObject':InstitutionObject})
						except:
							try:
								InstitutionObject = AboutInstitution.objects.filter(pincode = form['search'])
								return render(request,'info_1.html',{'into':into,'InstitutionObject':InstitutionObject})

							except:
								try:
									# user = request.user
									myuserObject = MyUser.objects.get(user = user)
									return render(request,'noResultLogin.html',{'into':into,'myuserObject':myuserObject})
								except:
									questionObject = AskQuestion.objects.latest('id')
									idS = questionObject.id
									questionObject1 = AskQuestion.objects.get(id = idS - 1)
									questionObject2= AskQuestion.objects.get(id = idS - 2)
									questionObject3 = AskQuestion.objects.get(id = idS - 3)
									questionObject4 = AskQuestion.objects.get(id = idS - 4)

									return render(request,'noResult.html',{'questionObject':questionObject,'questionObject1':questionObject1,'questionObject2':questionObject2,'questionObject3':questionObject3,'questionObject4':questionObject4,})

			except:
				try:
					user = request.user
					myuserObject = MyUser.objects.get(user = user)
					questionObject = AskQuestion.objects.latest('id')
					idS = questionObject.id
					questionObject1 = AskQuestion.objects.get(id = idS - 1)
					questionObject2= AskQuestion.objects.get(id = idS - 2)
					questionObject3 = AskQuestion.objects.get(id = idS - 3)
					questionObject4 = AskQuestion.objects.get(id = idS - 4)

					return render(request,'noResultLogin.html',{'questionObject':questionObject,'questionObject1':questionObject1,'questionObject2':questionObject2,'questionObject3':questionObject3,'questionObject4':questionObject4,'into':into,'myuserObject':myuserObject})
				except:
					questionObject = AskQuestion.objects.latest('id')
					idS = questionObject.id
					questionObject1 = AskQuestion.objects.get(id = idS - 1)
					questionObject2= AskQuestion.objects.get(id = idS - 2)
					questionObject3 = AskQuestion.objects.get(id = idS - 3)
					questionObject4 = AskQuestion.objects.get(id = idS - 4)

					return render(request,'noResult.html',{'questionObject':questionObject,'questionObject1':questionObject1,'questionObject2':questionObject2,'questionObject3':questionObject3,'questionObject4':questionObject4,})

		else:
			return redirect('/home/')

@csrf_exempt
def info(request):
	return render(request,'info.html')

@csrf_exempt
@login_required(login_url = '/loginP')
def AddInstitute(request):
	try:
		user = request.user
		myuserObject = MyUser.objects.get(user = user)
		first_name = user.first_name
		countryObjects = CountryMaster.objects.all()
		stateObjects = StateMaster.objects.all()
		cityObjects = CityMaster.objects.all()

		return render(request,'add_institute.html',{'first_name':first_name, 'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObjects':cityObjects})
	except:
		return redirect('/loginP/')
# def country(request):
# 	# countryObjects = CountryMaster.objects.all()
# 	stateObjects = StateMaster.objects.all()
# 	cityObjects = CityMaster.objects.all()

# 	if request.method == 'POST':
# 		form = request.POST

# 		countryObject = CountryMaster.objects.get(name = form['country'])

# 		stateObject = StateMaster.objects.filter(countryId = countryObject)
# 		return render(request,'add_institute_1.html',{'countryObject':countryObject,'stateObject':stateObject,})

# 	else:
# 		return render(request,'add_institute.html',{'stateObjects':stateObjects,'cityObjects':cityObjects})



# def state(request):
# 	# countryObjects = CountryMaster.objects.all()
# 	stateObjects = StateMaster.objects.all()
# 	cityObjects = CityMaster.objects.all()

# 	if request.method == 'POST':
# 		form = request.POST

# 		countryObject = form['country']
# 		state_Object = StateMaster.objects.get(name = form['state'])

# 		cityObject = CityMaster.objects.filter(stateId = state_Object)
# 		return render(request,'add_institute_2.html',{'countryObject':countryObject,'state_Object':state_Object,'cityObject':cityObject})

# 	else:
# 		return render(request,'add_institute.html',{'stateObjects':stateObjects,'cityObjects':cityObjects})
@csrf_exempt
@login_required(login_url = '/loginP')
def AddAnInstitution(request):
	user = request.user
	myuserObject = MyUser.objects.get(user = user)
	if request.method == "POST":
		form = request.POST

		Institution_name = form['institute_name']
		# established_year = form['year_established']
		board = form['board']
		typeS = form['type']
		category = form['category']
		website = form['website_name']
		contact_details = form['contact']
		person_to_contact = form['person_contact']
		email = form['email']
		country = CountryMaster.objects.get(name = form['country']) 
		state = StateMaster.objects.get(name = form['state'] )
		city = CityMaster.objects.get(name = form['city']) 
		address = form['address']
		pincode = form['pincode']

		description = form['description'] 

		InstitutionObject = AboutInstitution.objects.create(
			Institution_name = Institution_name.capitalize(),
			InstitutionCategory = category,
			school_board = board,
			InstitutionType = typeS,
			# established_year = established_year,
			contact_details = contact_details,
			addedBy = myuserObject,
			website = website,
			email = email,
			person_to_contact = person_to_contact.capitalize(),
			country = country,
			state = state,
			city = city,
			full_address = address.capitalize(),
			pincode = pincode.capitalize(),
			description = description.capitalize(),

			)
		questionObject = AskQuestion.objects.latest('id')
		idS = questionObject.id
		questionObject1 = AskQuestion.objects.get(id = idS - 1)
		questionObject2= AskQuestion.objects.get(id = idS - 2)
		questionObject3 = AskQuestion.objects.get(id = idS - 3)
		questionObject4 = AskQuestion.objects.get(id = idS - 4)

		return render(request,'home_to.html',{'Institution_name':Institution_name,'questionObject':questionObject,'questionObject1':questionObject1,'questionObject2':questionObject2,'questionObject3':questionObject3,'questionObject4':questionObject4,'myuserObject':myuserObject})
	else:
		return redirect('/home')

@csrf_exempt
@login_required(login_url = '/loginP')
def addReview(request):
	user = request.user
	myuserObject = MyUser.objects.get(user = user)
	if request.method == 'POST':
		form = request.POST


		Institution_Objects = AboutInstitution.objects.get(id = form['abc'])

		InstitutionObject = Institution_Objects

		reviewObject = ReviewAboutInstitution.objects.filter(InstitutionName = InstitutionObject)


		# abcd = form['institute_name']
		xyz = form['title']
		pqr = form['review']

		reviewObject_s = ReviewAboutInstitution.objects.create(
		
		InstitutionName = InstitutionObject,
		review_title = xyz.capitalize(),
		review = pqr.capitalize(),
		addedBy = myuserObject,
		addedDateTime = datetime.now().date()
		
		)
		myuserObject.Number_of_reviews +=1
		myuserObject.save()

		return render(request,'info.html',{'reviewObject':reviewObject,'InstitutionObject':InstitutionObject})
	else:
		pass

@csrf_exempt
def knowMore(request):
	try:
		user = request.user
		myuserObject = MyUser.objects.get(user = user)
		print(user)
		into = True
		if request.method == 'POST':
			form = request.POST

			id_got_is = form['knowId']

			InstitutionObject = AboutInstitution.objects.get(id = id_got_is)
			reviewObject = ReviewAboutInstitution.objects.filter(InstitutionName = InstitutionObject)

			return render(request,'info.html',{'into':into,'user':user,'InstitutionObject':InstitutionObject,'reviewObject':reviewObject})
		else:
			return HttpResponse('not done')
	except:
		into = False
		if request.method == 'POST':
			form = request.POST

			id_got_is = form['knowId']

			InstitutionObject = AboutInstitution.objects.get(id = id_got_is)
			reviewObject = ReviewAboutInstitution.objects.filter(InstitutionName = InstitutionObject)

			return render(request,'info.html',{'into':into,'InstitutionObject':InstitutionObject,'reviewObject':reviewObject})
		else:
			return HttpResponse('not done')


@csrf_exempt
def Register(request):
	countryObjects = CountryMaster.objects.all()
	stateObjects = StateMaster.objects.all()
	cityObjects = CityMaster.objects.all()

	return render(request,'register.html',{'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObjects':cityObjects})


@csrf_exempt
def registerYourself(request):
	countryObjects = CountryMaster.objects.all()
	stateObjects = StateMaster.objects.all()
	cityObjects = CityMaster.objects.all()
	
	if request.method == 'POST':
		form = request.POST

		first_name = form['first_name']
		last_name =  form['last_name']
		password = form['password']
		email = form['email']
		gender = form['gender']
		# image = form['file']
		mobile_number = form['contact']		
		country = CountryMaster.objects.get(name = form['country'])
		state = StateMaster.objects.get(name = form['state'])
		city = CityMaster.objects.get(name = form['city'])
		address = form['address']
		pincode = form['pincode']
		
		user = User.objects.create_user(
			username = email,
			first_name = first_name.capitalize(),
			last_name = last_name.capitalize(),
			email = email,
			password = password,
			)

		myuser = MyUser.objects.create(
			user = user,
			mobileNumber = mobile_number,
			gender = gender,
			country = country,
			state = state,
			city = city,
			full_address = address.capitalize(),
			pincode = pincode,
			isProfileComplete = False,
			is_activeYesNO = True,
			created_date_time = datetime.now().date()
			
			)
	
		subject = 'Thanaks for Registering'
		message = ' Thanks for registering on our site. We hope you will enjoy all the features provided. Search schools and ask question related to any topic and get discussion over that. All the Best!!!  By Instufind'
		from_email = settings.EMAIL_HOST_USER
		to_list = [email,settings.EMAIL_HOST_USER]
		send_mail(subject,message,from_email,to_list,fail_silently = True)

		return render(request,'successRegister.html',{'email':email})
	else:
		return redirect('/Register/')


# upload your images
@csrf_exempt
@login_required(login_url = '/loginP')
def listS(request):
    # Handle file upload
    user = request.user
    myuserObject = MyUser.objects.get(user = user)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(image=request.FILES['docfile'])
            newdoc.userId = myuserObject
            myuserObject.is_image_uploaded = True
            myuserObject.image_url = newdoc.image.url
            myuserObject.save()
            newdoc.save()
            print('image has been uploaded!!!')

            # Redirect to the document list after POST
            return redirect('/profile/')
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    # documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request,'profile.html',{'myuserObject': myuserObject, 'form': form})


#upload your institution images
@csrf_exempt
@login_required(login_url = '/loginP')
def listing(request):
    # Handle file upload
	user = request.user
	myuserObject = MyUser.objects.get(user = user)
	if request.method == 'POST':
		id_got = AboutInstitution.objects.get(id = id_of_inst)
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = AboutInstitution(image=request.FILES['docfile'])
			newdoc.userId = myuserObject
			newdoc.InstitutionName = id_got
			newdoc.save()
			print('image has been uploaded!!!')

            # Redirect to the document list after POST
			return redirect('/info/')
	else:
		form = DocumentForm()  # A empty, unbound form
		return render(request,'info.html',{'myuserObject': myuserObject, 'form': form})




@csrf_exempt
def loginPage(request):
	return render(request,'login.html')

@csrf_exempt
def loginAcc(request):
	a = 0
	questionObject = AskQuestion.objects.filter(is_answered_YesNo = False)
	for adf in questionObject:
		a += 1
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password = password)
	if user is not None:
		if user.is_active:
			try:
				login(request, user)
				
				first_name = user.first_name
				# emailReq = user.username

				userObject = MyUser.objects.get(user = user)
				userObject.is_loggedIn = True
				userObject.last_logged_in = datetime.now()
				userObject.save()
			except:
				messages.warning(request,"This account is not found!!")
				return render(request,'login.html')

			questionObject = AskQuestion.objects.latest('id')
			idS = questionObject.id
			questionObject1 = AskQuestion.objects.get(id = idS - 1)
			questionObject2= AskQuestion.objects.get(id = idS - 2)
			questionObject3 = AskQuestion.objects.get(id = idS - 3)
			questionObject4 = AskQuestion.objects.get(id = idS - 4)
			totalInstitution = AboutInstitution.objects.all().count()
			totalQuestion = AskQuestion.objects.all().count()
			totalComment = Comment.objects.all().count()
			return render(request,'login_home.html',{'totalComment':totalComment,'totalQuestion':totalQuestion,'totalInstitution':totalInstitution,'questionObject':questionObject,'questionObject1':questionObject1,'questionObject2':questionObject2,'questionObject3':questionObject3,'questionObject4':questionObject4,'first_name':first_name ,'a':a})
		else:
			print(3)
			messages.warning(request,"This account is not activated!!")
			return render(request,'login.html')

	else:
		print(4)
		messages.warning(request," Enter Correct username and password!!")
		return render(request,'login.html')


@csrf_exempt
@login_required(login_url = '/loginP')
def loginHome(request):
	questionObject = AskQuestion.objects.latest('id')
	idS = questionObject.id
	questionObject1 = AskQuestion.objects.get(id = idS - 1)
	questionObject2= AskQuestion.objects.get(id = idS - 2)
	questionObject3 = AskQuestion.objects.get(id = idS - 3)
	questionObject4 = AskQuestion.objects.get(id = idS - 4)
	totalInstitution = AboutInstitution.objects.all().count()
	totalQuestion = AskQuestion.objects.all().count()
	totalComment = Comment.objects.all().count()
	a = 0
	questionObject = AskQuestion.objects.filter(is_answered_YesNo = False)
	for adf in questionObject:
		a += 1
	user = request.user
	myuserObject = MyUser.objects.get(user = user)
	first_name = user.first_name

	return render(request,'login_home.html',{'totalComment':totalComment,'totalQuestion':totalQuestion,'totalInstitution':totalInstitution,'first_name':first_name,'a':a,'questionObject':questionObject,'questionObject1':questionObject1,'questionObject2':questionObject2,'questionObject3':questionObject3,'questionObject4':questionObject4,})


@csrf_exempt
@login_required(login_url='/loginP')
def user_logout(request):
	user = request.user
	myuserObject = MyUser.objects.get(user = user)
	myuserObject.is_loggedIn = False
	myuserObject.save()
	logout(request)
	return redirect('/loginP/')


@csrf_exempt
@login_required(login_url = '/loginP')
def profile(request):
	countryObjects = CountryMaster.objects.all()
	stateObjects = StateMaster.objects.all()
	cityObjects = CityMaster.objects.all()
	TopicObjects = TopicMaster.objects.all()
	
	user = request.user
	myuserObject = MyUser.objects.get(user = user)

	areaObject = SpecialisationMaster.objects.filter(userIs = myuserObject)

	form = DocumentForm()
	try:
		imageObject = Document.objects.get(userId = myuserObject)
		try:
			InstitutionObject = AboutInstitution.objects.filter(addedBy = myuserObject)
			return render(request,'profile.html',{'TopicObjects':TopicObjects, 'areaObject':areaObject, 'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObjects':cityObjects,'InstitutionObject':InstitutionObject,'form':form, 'imageObject':imageObject, 'myuserObject':myuserObject})
		except:
			return render(request,'profile.html',{'TopicObjects':TopicObjects, 'areaObject':areaObject, 'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObjects':cityObjects,'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObjects':cityObjects,'form':form, 'imageObject':imageObject, 'myuserObject':myuserObject})
	except:
		return render(request,'profile.html',{'TopicObjects':TopicObjects, 'areaObject':areaObject,'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObjects':cityObjects,'form':form,'myuserObject':myuserObject})


@csrf_exempt
@login_required(login_url = '/loginP')
def updateProfile(request):
	user = request.user
	if request.method == 'POST':
		form = request.POST
		profileObject = MyUser.objects.get(user = user)
		countryObject = CountryMaster.objects.get(name = form['country'])
		stateObject = StateMaster.objects.get(name = form['state'])
		cityObject = CityMaster.objects.get(name = form['city'])

		user.first_name = form['first_name']
		user.last_name = form['last_name']
		profileObject.gender = form['gender']
		profileObject.country = countryObject
		profileObject.state = stateObject
		profileObject.city = cityObject
		profileObject.full_address = form['address']
		profileObject.pincode = form['pincode']

		user.save()
		profileObject.save()
		return redirect('/profile/')
	else:
		return redirect('/profile/')




@csrf_exempt
# @login_required(login_url='/loginP')
def about_reviewer(request):
	try:
		into = True
		user = request.user
		myuserObject_9 = MyUser.objects.get(user = user)

		topics = TopicMaster.objects.all()
		if request.method == 'POST':
			form = request.POST

			userObject = User.objects.get(username = form['reviewId'])
			myuserObject = MyUser.objects.get(user = userObject)

			return render(request,'about_reviewer.html',{'into':into,'myuserObject':myuserObject,'topics':topics})
		else:
			return HttpResponse('not done')
	except:
		into = False
		topics = TopicMaster.objects.all()
		if request.method == 'POST':
			form = request.POST

			userObject = User.objects.get(username = form['reviewId'])
			myuserObject = MyUser.objects.get(user = userObject)

			return render(request,'about_reviewer.html',{'into':into,'myuserObject':myuserObject,'topics':topics})
		else:
			return HttpResponse('not done')



@csrf_exempt
@login_required(login_url = '/loginP')
def add_Question(request):
	try:
		user = request.user
		userAsked = MyUser.objects.get(user = user)

		if request.method == 'POST':
			form = request.POST

			user_id_get = form['abc']
			user_get = User.objects.get(username = user_id_get)
			myuserObject = MyUser.objects.get(user = user_get)

			Asked_Question = form['question'].capitalize()
			Asked_topic = TopicMaster.objects.get(name = form['topic'])

			AskQuestionObect = AskQuestion.objects.create(
				userAsked = userAsked,
				Asked_to = myuserObject,
				asked_date = datetime.now().date(),
				asked_time = datetime.now().time(),
				Asked_Question = Asked_Question,
				Ask_topic = Asked_topic,
				)			
			return redirect('/ask/')
		else:
			print(101)
			HttpResponse('not done')

	except:
		return HttpResponse('You must be logged in!!')


@csrf_exempt
@login_required(login_url = '/loginP')
def askFunction(request):
	user = request.user
	myuserObject = MyUser.objects.get(user = user)
	try:

		question_by_all_user = AskQuestion.objects.filter(userAsked = myuserObject).order_by('number_of_likes')

		return render(request,'ask.html',{'user':user,'question_by_all_user':question_by_all_user})
	except:
		return render(request,'ask.html')

@csrf_exempt
@login_required(login_url = '/loginP')
def answer_the_question(request):
	user = request.user
	myuserObject = MyUser.objects.get(user = user)
	
	try:
		question_to_answer = AskQuestion.objects.filter(Asked_to = myuserObject)
		return render(request,'answer_it.html',{'user':user,'question_by_all_user':question_to_answer})
	except:
		messages.warning(request,"Sorry No Question Found for you!!")
		return render(request,'answer_it.html',{'user':user,})


@csrf_exempt
@login_required(login_url = '/loginP')
def answer_the_question_DP(request):
	user = request.user
	myuserObject = MyUser.objects.get(user = user)

	if request.method == 'POST':
		form = request.POST

		questionId = form['abc']

		questionObject = AskQuestion.objects.get(id = questionId)
		questionObject.answer_is = form['answer']
		questionObject.is_answered_YesNo = True
		questionObject.Asked_to = myuserObject
		questionObject.answer_on_date = datetime.now().date()
		questionObject.answer_on_time = datetime.now().time()

		questionObject.save()


		return redirect('/discussionPage/')
	else:
		return redirect('/discussionPage/')


@csrf_exempt
@login_required(login_url = '/loginP')
def addAnswer(request):
	user = request.user
	if request.method == 'POST':
		form = request.POST

		questionId = form['abc']

		questionObject = AskQuestion.objects.get(id = questionId)
		questionObject.answer_is = form['answer']
		questionObject.is_answered_YesNo = True
		questionObject.answer_on_date = datetime.now().date()
		questionObject.answer_on_time = datetime.now().time()

		questionObject.save()

		return redirect('/answer_the_question/')
	else:
		return redirect('/answer_the_question/')

@csrf_exempt
@login_required(login_url = '/loginP')
def discussionPage_today(request):
	user = request.user
	myuserObject = MyUser.objects.get(user = user)
	date = datetime.now()
	AskQuestionObject = AskQuestion.objects.filter(asked_Date = date)
	topics = TopicMaster.objects.all()

	return render(request,'discussion.html',{'topics':topics,'myuserObject':myuserObject,'AskQuestionObject':AskQuestionObject})


@csrf_exempt
@login_required(login_url = 'loginP')
def askQuestion_DP(request):
	try:
		user = request.user
		userAsked = MyUser.objects.get(user = user)

		if request.method == 'POST':
			form = request.POST

			user_id_get = form['abc']
			user_get = User.objects.get(username = user_id_get)
			myuserObject = MyUser.objects.get(user = user_get)

			Asked_Question = form['question'].capitalize()
			Asked_topic = TopicMaster.objects.get(name = form['topic'])

			AskQuestionObect = AskQuestion.objects.create(
				userAsked = userAsked,
				# Asked_to = myuserObject,
				Asked_Question = Asked_Question,
				Ask_topic = Asked_topic,
				)			
			return redirect('/ask/')
		else:
			print(101)
			HttpResponse('not done')

	except:
		return redirect('/loginP/')



@csrf_exempt
def discussionPage(request):
	try:
		user = request.user
		myuserObject = MyUser.objects.get(user = user)
		topics = TopicMaster.objects.all()
		AskQuestionObject = AskQuestion.objects.all().order_by('-id')

		return render(request,'discussion.html',{'topics':topics,'myuserObject':myuserObject,'AskQuestionObject':AskQuestionObject})
	except:
		topics = TopicMaster.objects.all()
		AskQuestionObject = AskQuestion.objects.all().order_by('-id')

		return render(request,'discussion.html',{'topics':topics,'AskQuestionObject':AskQuestionObject})


# views for filter post of last seven days

@csrf_exempt
def discussionPage_last_seven_days(request):
	try:
		user = request.user
		myuserObject = MyUser.objects.get(user = user)
		startdate = datetime.today()
		enddate = startdate - timedelta(days = 6)
		topics = TopicMaster.objects.all()

		AskQuestionObject = AskQuestion.objects.all().filter(asked_Date__gte = enddate).order_by('-id')
		for obj in AskQuestionObject:
			print(obj)

		return render(request,'discussion.html',{'topics':topics,'myuserObject':myuserObject,'AskQuestionObject':AskQuestionObject})
	except:
		startdate = datetime.today()
		enddate = startdate - timedelta(days = 6)
		topics = TopicMaster.objects.all()

		AskQuestionObject = AskQuestion.objects.all().filter(asked_Date__gte = enddate).order_by('-id')
		for obj in AskQuestionObject:
			print(obj)

		return render(request,'discussion.html',{'topics':topics,'AskQuestionObject':AskQuestionObject})


@csrf_exempt
def discussionPage_last_thirty_days(request):
	try:
		user = request.user
		myuserObject = MyUser.objects.get(user = user)
		startdate = datetime.today()
		enddate = startdate - timedelta(days = 30)
		topics = TopicMaster.objects.all()

		AskQuestionObject = AskQuestion.objects.all().filter(asked_Date__gte = enddate).order_by('-id')
		for obj in AskQuestionObject:
			print(obj)

		return render(request,'discussion.html',{'topics':topics,'myuserObject':myuserObject,'AskQuestionObject':AskQuestionObject})

	except:
		startdate = datetime.today()
		enddate = startdate - timedelta(days = 30)
		topics = TopicMaster.objects.all()

		AskQuestionObject = AskQuestion.objects.all().filter(asked_Date__gte = enddate).order_by('-id')
		for obj in AskQuestionObject:
			print(obj)

		return render(request,'discussion.html',{'topics':topics,'AskQuestionObject':AskQuestionObject})


@csrf_exempt
@login_required(login_url = '/loginP')
def likes_answer(request):
	try:
		user = request.user
		myuserObject = MyUser.objects.get(user = user)

		if request.method == 'POST':
			post = request.POST

			id_got = post['id_required']
			AskQuestionObject = AskQuestion.objects.get(id = id_got)
			topicObject = AskQuestionObject.Ask_topic

			try:

				likes_object = likes.objects.filter(likes_object = AskQuestionObject)

				# try:
				a = 0
				# likes_object.filter(liked_by = myuserObject)
				print('object found')
				for obj in likes_object:
					if obj.liked_by == myuserObject:
						a += 1
						return HttpResponse('You have liked this!!')

				if a != 1:
					print('object not found!!')
					likesObject = likes.objects.create(
						liked_by = myuserObject,
						like_type = 'Answer',
						likes_object = AskQuestionObject,
						object_topic = topicObject,
						)
					AskQuestionObject.number_of_likes +=1
					AskQuestionObject.save()
					return redirect('/discussionPage/')

			except:
				print(120)
				likesObject = likes.objects.create(
					liked_by = myuserObject,
					like_type = 'Answer',
					likes_object = AskQuestionObject,
					object_topic = topicObject	,
					)
				AskQuestionObject.number_of_likes +=1
				AskQuestionObject.save()
				return redirect('/discussionPage/')
			return HttpResponseNotFound('<h1>Page not found</h1>')
		else:
			return redirect('/discussionPage/')
	except:
		return HttpResponseNotFound('<h1>Page not found</h1>')


@csrf_exempt
@login_required(login_url = '/loginP')
def searchQuestionS(request):
	user = request.user

	if request.method == 'POST':
		form = request.POST

		querryObject = form['search'].capitalize()
		try:
			try:
				searchObject = TopicMaster.objects.get(name = querryObject)
				AskQuestionObject = AskQuestion.objects.filter(Ask_topic = searchObject).order_by('-asked_Date')
				return render(request,'discussion.html',{'user':user,'AskQuestionObject':AskQuestionObject})
			except:
				try:
					AskQuestionObject = AskQuestion.objects.filter(Asked_Question = querryObject)
					return render(request,'discussion.html',{'user':user,'AskQuestionObject':AskQuestionObject})
				except:
					messages.warning(request,'No result found!!')
					return redirect('/discussionPage/')
		except:
			messages.warning(request,'No result found!!')
			return redirect('/discussionPage/')


@csrf_exempt
def contactPage(request):
	if request.method == 'POST':
		form = request.POST
		name = form['name']
		email = form['email']
		subject = form['subject']
		message = form['message']

		helpObject = Help_Contact.objects.create(
			name = name,
			email = email,
			subject = subject,
			message = message,
			)
		message = "Your message has been sent. We will try to contact you soon.!!"
		return render(request,'index.html',{'message':message})
	else:
		return render(request,'index.html')


@csrf_exempt
@login_required(login_url = '/loginP')
def makeYourComment(request):
	user = request.user
	myuserObject = MyUser.objects.get(user = user)

	if request.method == 'POST':
		form = request.POST
		questionId = AskQuestion.objects.get(id = form['abcId'])
		CommentsAre = Comment.objects.filter(Question_is = questionId)
		commentContent = form['comment']

		commentObject = Comment.objects.create(
			Question_is = questionId,
			comment_Content = commentContent,
			comment_date = datetime.now().date(),
			comment_time = datetime.now().time(),
			comment_by = myuserObject,
			)

		questionId.number_of_comments+=1
		questionId.save()
		
		return render(request,'commentQuestion.html',{'CommentsAre':CommentsAre,'questionId':questionId,'myuserObject':myuserObject})
	else:
		return HttpResponse('not Done')

@csrf_exempt
@login_required(login_url = '/loginP')
def add_your_article(request):
	return render(request,'addArticle.html')

@csrf_exempt
@login_required(login_url = '/loginP')
def Your_article_is(request):
	user = request.user
	myuserObject = MyUser.objects.get(user = user)
	if request.method == 'POST':
		form = request.POST

		heading = form['heading']
		about = form['about']
		article = form['article']

		articleObject = YourArticle.objects.create(
			addedBy = myuserObject,
			article_heading = heading,
			article_is = article,
			article_about = about,
			article_date = datetime.now().date(),
			article_time = datetime.now().time()
			)
		return redirect('/show_your_article/')
	else:
		return redirect('/add_your_article/')


@csrf_exempt
def show_your_article(request):
	try:
		user = request.user
		myuserObject = MyUser.objects.get(user = user)
		ArticleObject = YourArticle.objects.all().order_by('-article_date')
		return render(request,'showArticle.html',{'myuserObject':myuserObject,'ArticleObject':ArticleObject})
	except:
		ArticleObject = YourArticle.objects.all().order_by('-article_date')
		return render(request,'showArticle.html',{'ArticleObject':ArticleObject})

@csrf_exempt
@login_required(login_url = '/loginP')
def show_my_article(request):
	try:
		user = request.user
		myuserObject = MyUser.objects.get(user = user)
		ArticleObject = YourArticle.objects.filter(addedBy = myuserObject).order_by('-article_date')
		return render(request,'showArticle.html',{'ArticleObject':ArticleObject,'myuserObject':myuserObject})
	except:
		return redirect('/loginP')


@csrf_exempt
def discussQ(request):
	try:
		user = request.user
		myuserObject = MyUser.objects.get(user = user)
		if request.method == 'POST':
			post = request.POST
			questionId = AskQuestion.objects.get(id = post['idSend'])
			CommentsAre = Comment.objects.filter(Question_is = questionId)
			return render(request,'commentQuestion.html',{'CommentsAre':CommentsAre,'questionId':questionId})

		else:
			return redirect('/discussionPage/')
	except:
		if request.method == 'POST':
			post = request.POST
			questionId = AskQuestion.objects.get(id = post['idSend'])
			CommentsAre = Comment.objects.filter(Question_is = questionId)
			return render(request,'commentQuestion.html',{'CommentsAre':CommentsAre,'questionId':questionId})

		else:
			return redirect('/discussionPage/')
@csrf_exempt
def article1(request):
	try:
		user = request.user
		myuserObject = MyUser.objects.get(user = user)
		return render(request,'article1.html',{'myuserObject':myuserObject})
	except:
		return render(request,'article1.html',{})


@csrf_exempt
def governmentSchool(request):
	try:
		into = True
		user = request.user
		myuserObject = MyUser.objects.get(user = user)
		InstitutionObject = AboutInstitution.objects.filter(InstitutionCategory = 'School' ,InstitutionType = 'Government')
		return render(request,'info_1.html',{'InstitutionObject':InstitutionObject, 'into':into,'myuserObject':myuserObject})
	except:
		into = False
		InstitutionObject = AboutInstitution.objects.filter(InstitutionCategory = 'School', InstitutionType = 'Government')
		return render(request,'info_1.html',{'InstitutionObject':InstitutionObject, 'into':into,})


@csrf_exempt
def privateSchool(request):
	try:
		into = True
		user = request.user
		myuserObject = MyUser.objects.get(user = user)
		InstitutionObject = AboutInstitution.objects.filter(InstitutionCategory = 'School' ,InstitutionType = 'Private')
		return render(request,'info_1.html',{'InstitutionObject':InstitutionObject, 'into':into,'myuserObject':myuserObject})
	except:
		into = False
		InstitutionObject = AboutInstitution.objects.filter(InstitutionCategory = 'School', InstitutionType = 'Private')
		return render(request,'info_1.html',{'InstitutionObject':InstitutionObject, 'into':into,})

@csrf_exempt
def coaching(request):
	try:
		into = True
		user = request.user
		myuserObject = MyUser.objects.get(user = user)
		InstitutionObject = AboutInstitution.objects.filter(InstitutionCategory = 'Coaching' ,InstitutionType = 'Private')
		return render(request,'info_1.html',{'InstitutionObject':InstitutionObject, 'into':into,'myuserObject':myuserObject})
	except:
		into = False
		InstitutionObject = AboutInstitution.objects.filter(InstitutionCategory = 'Coaching', InstitutionType = 'Private')
		return render(request,'info_1.html',{'InstitutionObject':InstitutionObject, 'into':into,})


def conc(request):
	return render(request,'dashboard.html')

@csrf_exempt
@login_required(login_url = '/loginP')
def commentOnArticle(request):
	user = request.user
	myuserObject = MyUser.objects.get(user = user)
	
	if request.method == 'POST':
		post = request.POST

		YourArticleObject = YourArticle.objects.get(id = post['artObj'])
		YourArticleObject.number_of_comments +=1
		YourArticleObject.save()

		abc = post['comment']
		newComment = CommentArticle.objects.create(
			Article_is = YourArticleObject,
			comment_Content = abc,
			comment_date = datetime.now().date(),
			comment_time = datetime.now().time(),
			comment_by = myuserObject
			)

		return HttpResponse('Your comment is submitted!!!')

	else:
		return HttpResponse('done')


def searchInstituteBs(request):
	
	# user = request.user
	# myuserObject = MyUser.objects.get(user = user)

	if request.method == 'POST':
		form = request.POST
		abcdIs = form['searchN'].capitalize()
		try:
			into = True
			stateObjects = StateMaster.objects.get(name = abcdIs)
			InstitutionObject = AboutInstitution.objects.filter(state__name__contains = stateObjects)
			return render(request,'info_1.html',{'InstitutionObject':InstitutionObject, 'into':into,'myuserObject':myuserObject})
		except:
			try:
				into = True
				cityObjects = CityMaster.objects.get(name = abcdIs)
				InstitutionObject = AboutInstitution.objects.filter(city__name__contains = cityObjects)
				return render(request,'info_1.html',{'InstitutionObject':InstitutionObject, 'into':into,'myuserObject':myuserObject})
			except:
				messages.warning(request,'No results found!!')
				return render(request,'info_1.html')
	else:
		return HttpResponse('not done')

@csrf_exempt
@login_required(login_url = '/loginP')
def addYourSpecial(request):
	# try:
	user = request.user
	myuserObject = MyUser.objects.get(user = user)
		
	if request.method == 'POST':
		form = request.POST

		topicIs = TopicMaster.objects.get(name = form['topicIs'])

		SpecialisationMasterNew = SpecialisationMaster.objects.create(
			userIs = myuserObject,
			areaOfSpecialisation = topicIs,
			addedOn = datetime.now().date()

			)
		return redirect('/profile/')
	else:
		return redirect('/profile/')

	# except:
	# 	return redirect('/loginP/')




#delete your area of spl
def deleteSpl(request):
	if request.method == 'POST':
		post = request.POST

		id_got = post['id_required']

		objectDeleteIs = SpecialisationMaster.objects.get(id = id_got)
		objectDeleteIs.delete()
		return redirect('/profile/')


#read Your article
def articleInfo(request,id):

	try:
		user = request.user
		myuserObject = MyUser.objects.get(user = user)
		
		YourArticleIs = YourArticle.objects.get(id=id)

		return render(request,'thisArticle.html',{'myuserObject':myuserObject,'YourArticleIs':YourArticleIs})
	except:
		YourArticleIs = YourArticle.objects.get(id=id)

		return render(request,'thisArticle.html',{'YourArticleIs':YourArticleIs})
