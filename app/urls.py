from django.conf.urls import url, include
from .views import teacher, student, course, game, home


student_urls = [
    url(r'^/?$', student.login_form, name='student_login'),
    url(r'^auth/?$', student.auth, name='student_auth'),
    url(r'^home/?$', student.login, name='student_home'),
    url(r'^create/(?P<course_id>\d+)?$', student.create, name='student_create'),
    url(r'^delete/(?P<user_id>\d+)/(?P<course_id>\d+)?$', student.delete, name='student_delete'),
    url(r'^store/?$', student.store, name='student_store'),
    url(r'^storeCSV/?$', student.storeCSV, name='student_storeCSV'),
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
    url(r'^update/?$', course.update, name='courses_update'),
    url(r'^(?P<course_id>\d+)/param/?$', course.param, name='courses_param'),
    url(r'^(?P<course_id>\d+)/edit/?$', course.edit, name='courses_edit'),
    url(r'^delete/(?P<course_id>\d+)/?$', course.delete, name='courses_delete'),
]

game_urls = [
    url(r'^(?P<game_id>\d+)/?$', game.see, name='game'),
]

urlpatterns = [
    url(r'^/?$', home.see, name='home'),
    url(r'^teacher/', include(teacher_urls)),
    url(r'^student/', include(student_urls)),
    url(r'^course/', include(course_urls)),
    url(r'^game/', include(game_urls)),
]
