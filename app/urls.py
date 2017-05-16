from django.conf.urls import url
from .views import teacher

urlpatterns = [
	url(r'^teacher/$', teacher.test, name='auth_teacher'),
]