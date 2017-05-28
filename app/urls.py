from django.conf.urls import url
from .views import teacher

urlpatterns = [
	url(r'^teacher/$', teacher.see, name='teacher_login'),
	url(r'^teacher/auth$', teacher.auth, name='teacher_auth'),
	url(r'^teacher/home', teacher.home, name='teacher_home'),
	url(r'^teacher/logout', teacher.home, name='teacher_logout'),
]