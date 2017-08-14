from django.conf.urls import include, url
from django.contrib import admin
from coachingApp import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    # Examples:
    # url(r'^$', 'myCoach.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'coachingApp.views.homepage', name='home'),
    url(r'^', include('coachingApp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
