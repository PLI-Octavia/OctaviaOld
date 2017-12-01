from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
import json
from app.models import Course, Game, GameCourse, Score, User, UserCourse, GameConfig

TEMPLATES_PATH = 'game/'

@login_required
def see(request, game_id):
    game = Game.objects.get(pk=game_id)
    uc = UserCourse.objects.get(user=request.user)
    if GameConfig.objects.filter(course_id=uc.course.id, game_id=game.id) :
        config = GameConfig.objects.filter(course_id=uc.course.id, game_id=game.id).get()
        nb = json.loads(config.config)
        nb = nb['value']
    else :
        nb = -1

    
    # Game folder name in static/games must be the game name.
    return render(request, TEMPLATES_PATH + 'show.html', {"game_name": game.name, "user":request.user, 'game_id':game.id, 'nb':nb})

#list all of the game avaible
@login_required
def for_course(request, course_id):
    games = Game.objects.all()
    course = Course.objects.get(pk=course_id)
    course_games = course.games.all()
    games_with_flag = [(game, game in course_games) for game in games]
    student = request.GET.get('student', 0)
    return render(request, TEMPLATES_PATH + 'for_course.html', {'games_with_flag': games_with_flag, 'course_id': course_id, 'student': student})

#Activate game for course
@login_required
def enable_for_course(request, course_id, game_id):
    course = Course.objects.get(pk=course_id)
    game = Game.objects.get(pk=game_id)
    game_course = GameCourse(course=course, game=game)
    game_course.save()

    return redirect('game_for_course', course_id=course_id)

#Disable game for course
@login_required
def disable_for_course(request, course_id, game_id):
    GameCourse.objects.filter(course_id=course_id, game_id=game_id).delete()

    return redirect('game_for_course', course_id=course_id)

#See stat
@login_required
def stats(request, game_id):
    scores = Score.objects.filter(game_id=game_id).select_related('student')
    users = User.objects.all()
    scores_json = serializers.serialize('json', scores)
    users_json = serializers.serialize('json', users)
    
    return render(request, TEMPLATES_PATH + 'stats.html', {
        'scores_json': scores_json,
        'users_json': users_json,
    })
