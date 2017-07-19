from django.conf.urls import url,patterns
from coachingApp.views import *

urlpatterns = [
	url(r'^home/',homepage,name='homepage'),
	url(r'^search/',search,name='search'),
	url(r'^info/',info,name='info'),
	url(r'^AddInstitute/',AddInstitute,name='AddInstitute'),
	url(r'^addReview/',addReview,name='addReview'),
	url(r'^AddAnInstitution/',AddAnInstitution,name='AddAnInstitution'),
	url(r'^knowMore/',knowMore,name='knowMore'),
	url(r'^Register/',Register,name='Register'),
	url(r'^registerYourself/',registerYourself,name='registerYourself'),
	url(r'^loginP/',loginPage,name='loginShow'),
	url(r'^login/',loginAcc,name='login'),
	url(r'^loginHome/',loginHome,name='loginHome'),
	url(r'^logout/',user_logout,name='logout'),
	url(r'^about_reviewer/',about_reviewer,name='logout'),
	url(r'^askQuestion/',add_Question,name='logout'),
	url(r'^ask/',askFunction,name='logout'),
	url(r'^answer_the_question/',answer_the_question,name='logout'),
	url(r'^addAnswer/',addAnswer,name='logout'),
	url(r'^discussionPage/',discussionPage,name='discussionPage'),
	url(r'^discussionPage_today/',discussionPage_today,name='discussionPage'),
	url(r'^discussionPage_last_seven_days/',discussionPage_last_seven_days,name='discussionPage'),
	url(r'^discussionPage_last_thirty_days/',discussionPage_last_thirty_days,name='discussionPage'),
	url(r'^profile/',profile,name='discussionPage'),
	url(r'^askQuestion_DP/',askQuestion_DP,name='discussionPage'),
	url(r'^answer_the_question_DP/',answer_the_question_DP,name='answer_the_question_DP'),
	url(r'^upload/',listS,name='answer_the_question_DP'),
	url(r'^likes_answer/',likes_answer,name='likes_answer'),
	url(r'^searchQuestionS/',searchQuestionS,name='likes_answer'),

	]