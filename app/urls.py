from django.conf.urls import url, include
from .views import teacher, student, course, game, home, score, config


student_urls = [
    url(r'^/?$', student.login_form, name='student_login'),
    url(r'^auth/?$', student.auth, name='student_auth'),
    url(r'^home/?$', student.login, name='student_home'),
    url(r'^create/(?P<course_id>\d+)?$', student.create, name='student_create'),
    url(r'^delete/(?P<user_id>\d+)/(?P<course_id>\d+)?$', student.delete, name='student_delete'),
    url(r'^update/(?P<user_id>\d+)/(?P<course_id>\d+)?$', student.update, name='student_update'),
    url(r'^store/?$', student.store, name='student_store'),
    url(r'^save/?$', student.save, name='student_save'),
    url(r'^storeCSV/?$', student.storeCSV, name='student_storeCSV'),
]

teacher_urls = [
    url(r'^$', teacher.see, name='teacher_login'),
    url(r'^auth/?$', teacher.auth, name='teacher_auth'),
    url(r'^home/?$', teacher.home, name='teacher_home'),
    url(r'^logout/?$', teacher.logout, name='teacher_logout')
]

course_urls = [
    url(r'^/?$', course.see, name='courses'),
    url(r'^create/?$', course.create, name='courses_create'),
    url(r'^store/?$', course.store, name='courses_store'),
    url(r'^update/?$', course.update, name='courses_update'),
    url(r'^(?P<course_id>\d+)/param/?$', course.param, name='courses_param'),
    url(r'^(?P<course_id>\d+)/edit/?$', course.edit, name='courses_edit'),
    url(r'^delete/(?P<course_id>\d+)/?$', course.delete, name='courses_delete'),

    # cross-reference URLs
    url('^(?P<course_id>\d+)/game/?$', game.for_course, name='game_for_course'),
    url('^(?P<course_id>\d+)/game/(?P<game_id>\d+)/enable/?$', game.enable_for_course, name='game_enable_for_course'),
    url('^(?P<course_id>\d+)/game/(?P<game_id>\d+)/disable/?$', game.disable_for_course, name='game_enable_for_course'),
]

game_urls = [
    url(r'^upload/?$', game.upload, name='game_upload'),
    url(r'^(?P<game_id>\d+)/?$', game.see, name='game'),
    url(r'^(?P<game_id>\d+)/scores/?$', game.stats, name='game_scores'),
]

score_urls = [
    url(r'^(?P<user_id>\d+)/(?P<game_id>\d+)/?$', score.store, name='score_store'),
]

config_urls = [
    url(r'^(?P<game_id>\d+)/(?P<course_id>\d+)/?$', config.see, name='config_see'),
    url(r'^store/?$', config.store, name='config_store'),
]

urlpatterns = [
    url(r'^/?$', student.auth, name='home'),
    url(r'^teacher/', include(teacher_urls)),
    url(r'^student/', include(student_urls)),
    url(r'^course/', include(course_urls)),
    url(r'^game/', include(game_urls)),
    url(r'^score/', include(score_urls)),
    url(r'^config/', include(config_urls)),
]
