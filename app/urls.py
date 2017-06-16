from django.conf.urls import url, include
from .views import teacher, student, course

student_urls = [
    url(r'^/?$', student.login_form, name='student_login'),
    url(r'^auth/?$', student.auth, name='student_auth'),
    url(r'^home/?$', student.login, name='student_login'),
    url(r'^create/?$', student.create, name='student_create'),
    url(r'^store/?$', student.store, name='student_store'),
]

teacher_urls = [
    url(r'^/?$', teacher.see, name='teacher_login'),
    url(r'^auth/?$', teacher.auth, name='teacher_auth'),
    url(r'^home/?$', teacher.home, name='teacher_home'),
    url(r'^logout/?$', teacher.home, name='teacher_logout')
]

course_urls = [
    url(r'^/?$', course.see, name='courses'),
    url(r'^create/?$', course.create, name='courses_create'),
    url(r'^store/?$', course.store, name='courses_store'),
]

urlpatterns = [
    url(r'^teacher/', include(teacher_urls)),
    url(r'^student/', include(student_urls)),
    url(r'^course/', include(course_urls)),

]
