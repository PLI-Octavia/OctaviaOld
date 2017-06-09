from django.conf.urls import url, include
from .views import teacher, student

student_urls = [
    url(r'^/?$', student.login_form, name='student_login'),
    url(r'^auth/?$', student.auth, name='student_auth'),
    url(r'^home/?$', student.login, name='student_login'),
]

urlpatterns = [
	url(r'^teacher/$', teacher.see, name='teacher_login'),
	url(r'^teacher/auth$', teacher.auth, name='teacher_auth'),
	url(r'^teacher/home$', teacher.home, name='teacher_home'),
	url(r'^teacher/logout$', teacher.home, name='teacher_logout'),
	url(r'^course/$', course.see, name='courses'),
	url(r'^course/create$', course.create, name='courses_create'),
	url(r'^course/store$', course.store, name='courses_store'),
    url(r'^student/', include(student_urls))

]