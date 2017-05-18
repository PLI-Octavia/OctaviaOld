from django.conf.urls import url
from .views import teacher

urlpatterns = [
	url(r'^teacher/$', teacher.see, name='auth_teacher'),
	url(r'^teacher/auth$', teacher.auth, name='auth_teacher'),
]