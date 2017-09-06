from django.shortcuts import render, redirect
from app.models import Course, Game, GameCourse

TEMPLATES_PATH = 'game/'


def see(request, game_id):
    game = Game.objects.get(pk=game_id)

    # Game folder name in static/games must be the game name.
    return render(request, TEMPLATES_PATH + 'show.html', {"game_name": game.name})

def for_course(request, course_id):
    games = Game.objects.all()
    course = Course.objects.get(pk=course_id)
    course_games = course.games.all()
    games_with_flag = [(game, game in course_games) for game in games]

    return render(request, TEMPLATES_PATH + 'for_course.html', {'games_with_flag': games_with_flag, 'course_id': course_id})

def enable_for_course(request, course_id, game_id):
    course = Course.objects.get(pk=course_id)
    game = Game.objects.get(pk=game_id)
    game_course = GameCourse(course=course, game=game)
    game_course.save()

    return redirect('game_for_course', course_id=course_id)

def disable_for_course(request, course_id, game_id):
    GameCourse.objects.filter(course_id=course_id, game_id=game_id).delete()

    return redirect('game_for_course', course_id=course_id)
