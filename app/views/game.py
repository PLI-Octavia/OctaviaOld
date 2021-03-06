from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.core.management import call_command
import json
import zipfile
from app.models import Course, Game, GameCourse, Score, User, UserCourse, GameConfig

TEMPLATES_PATH = 'game/'

@login_required
def see(request, game_id):
    game = Game.objects.get(pk=game_id)
    uc = None
    if 'course_id' in request.session:
        uc = UserCourse.objects.get(user=request.user, course_id=request.session['course_id']) # teacher has a class
    else:
        uc = UserCourse.objects.filter(user=request.user).first() # use .filter.first instead of .get because of teachers might have more than one class
    gc = GameConfig.objects.filter(course_id=uc.course.id, game_id=game.id).first()
    if gc:
        config = gc.config
    else:
        config = '{}'

    # Game folder name in static/games must be the game name.
    return render(request, TEMPLATES_PATH + 'show.html', {"game_name": game.name, "user":request.user, 'game_id':game.id, 'config':json.dumps(config)})

#list all of the game avaible
@login_required
def for_course(request, course_id):
    request.session['course_id'] = course_id
    games = Game.objects.all()
    course = Course.objects.get(pk=course_id)
    request.session['course_name'] = course.name 
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

from tempfile import NamedTemporaryFile
from os.path import isfile
from django.contrib.staticfiles.templatetags.staticfiles import static 
from shutil import rmtree
from pathlib import Path
def uploadGameZip(name, zipFile):
    # TODO check if zipfile.ZipFile needs an actual file
    #      or if we can just use request.FILES directly
    with NamedTemporaryFile(suffix = '.zip') as tmp:
        with open(tmp.name, 'wb+') as dest:
            for chunk in zipFile.chunks():
                dest.write(chunk)
        with zipfile.ZipFile(tmp.name, 'r') as zf:
            game_path = 'app/static/games/' + name
            try:
                zf.extractall(game_path)
                configFile = Path(game_path + '/config.json')
                try:
                    with configFile.open() as f:
                        return f.read()
                except OSError:
                    return '{}'
            except:
                rmtree(game_path, ignore_errors=True)


from django.shortcuts import redirect

@login_required
def upload(request):
    if request.method == 'POST':
        game = Game()
        game.name = request.POST.get("name", "default")
        game.version = 1 # TODO parse from zip
        game.level = 1
        game.text = "Games"

        # TODO check if it's a zip etc
        metadata = uploadGameZip(game.name, request.FILES['gamefile'])
        if metadata is None:
            return render(request, TEMPLATES_PATH + 'upload.html', {'error': True})
        else:
            game.config = metadata
            game.save()
            call_command('collectstatic', verbosity=0, interactive=False)
            return redirect('/course/')
    else:
        return render(request, TEMPLATES_PATH + 'upload.html')
    
