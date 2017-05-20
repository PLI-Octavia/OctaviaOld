from django.conf.urls import url
from .views import teacher

urlpatterns = [
	url(r'^teacher/$', teacher.see, name='login_teacher'),
	url(r'^teacher/auth$', teacher.auth, name='auth_teacher'),
	url(r'^teacher/home', teacher.home, name='home_teacher'),
	url(r'^teacher/logout', teacher.home, name='logout_teacher'),
]