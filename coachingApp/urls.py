from django.conf.urls import url
from coachingApp.views import *

urlpatterns = [
	url(r'^home/$',homepage,name='homepage'),
	url(r'^search/$',search,name='search'),
	url(r'^info/$',info,name='info'),
	url(r'^AddInstitute/$',AddInstitute,name='AddInstitute'),
	url(r'^addReview/$',addReview,name='addReview'),
	url(r'^AddAnInstitution/$',AddAnInstitution,name='AddAnInstitution'),
	url(r'^knowMore/$',knowMore,name='knowMore'),
	url(r'^Register/$',Register,name='Register'),
	url(r'^registerYourself/$',registerYourself,name='registerYourself'),
	url(r'^loginP/$',loginPage,name='loginShow'),
	url(r'^login/$',loginAcc,name='login'),
	url(r'^loginHome/$',loginHome,name='loginHome'),
	url(r'^logout/$',user_logout,name='logout'),
	url(r'^about_reviewer/$',about_reviewer,name='logout'),
	url(r'^askQuestion/$',add_Question,name='logout'),
	url(r'^ask/$',askFunction,name='logout'),
	url(r'^answer_the_question/$',answer_the_question,name='logout'),
	url(r'^addAnswer/$',addAnswer,name='logout'),
	url(r'^discussionPage/$',discussionPage,name='discussionPage'),
	url(r'^discussionPage_today/$',discussionPage_today,name='discussionPage'),
	url(r'^discussionPage_last_seven_days/$',discussionPage_last_seven_days,name='discussionPage'),
	url(r'^discussionPage_last_thirty_days/$',discussionPage_last_thirty_days,name='discussionPage'),
	url(r'^profile/$',profile,name='discussionPage'),
	url(r'^askQuestion_DP/$',askQuestion_DP,name='discussionPage'),
	url(r'^answer_the_question_DP/$',answer_the_question_DP,name='answer_the_question_DP'),
	url(r'^upload/$',listS,name='upload your profile picture'),
	url(r'^likes_answer/$',likes_answer,name='likes_answer'),
	url(r'^searchQuestionS/$',searchQuestionS,name='likes_answer'),
	url(r'^uploadInst/$',listing,name='upload_your_institution Images'),
	url(r'^contactPage/$',contactPage,name='contactPage'),
	url(r'^updateProfile/$',updateProfile,name='updateProfile'),
	url(r'^makeYourComment/$',makeYourComment,name='makeYourComment'),
	url(r'^add_your_article/$',add_your_article,name='add_your_article'),
	url(r'^Your_article_is/$',Your_article_is,name='Your_article_is'),
	url(r'^show_your_article/$',show_your_article,name='Your_article_is'),
	url(r'^show_my_article/$',show_my_article,name='Your_article_is'),
	url(r'^discussQ/$',discussQ,name='discussQ'),
	url(r'^article1/$',article1,name='article1'),
	url(r'^privateSchool/$',privateSchool,name='privateSchool'),
	url(r'^governmentSchool/$',governmentSchool,name='governmentSchool'),
	url(r'^coaching/$',coaching,name='coaching'),
	url(r'^commentArticle/$',commentOnArticle,name='commentOnArticle'),
	url(r'^searchInstituteBs/$',searchInstituteBs,name='commentOnArticle'),
	url(r'^addYourSpecial/$',addYourSpecial,name='addYourSpecial'),
	url(r'^deleteSpl/$',deleteSpl,name='deleteSpl'),
	url(r'^article/(?P<id>\d+)/$',articleInfo,name='articleInfo'),

	]