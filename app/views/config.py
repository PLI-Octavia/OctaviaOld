from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
import json
import pprint

from app.models import Course, Game, GameCourse , User, GameConfig

TEMPLATES_PATH = 'config/'


def see(request, game_id, course_id):
	game = Game.objects.get(pk=game_id)
	
	models = game.config
	if request.GET.get('validate') == 1 :
		validate = 1
	else :
		validate = 0

	return render(request, TEMPLATES_PATH + 'see.html', {'models': models, 'course_id': course_id, 'game_id':game_id, 'validate': validate})

def store(request):
	game = Game.objects.get(pk=request.POST['game_id'])
	
	if GameConfig.objects.filter(course_id=request.POST['course_id'], game_id=request.POST['game_id']) :
		config = GameConfig.objects.filter(course_id=request.POST['course_id'], game_id=request.POST['game_id']).get()
		config.config = json.dumps({'value' : request.POST['conf']})
		config.save()
	else :
		config = GameConfig()
		config.game = game
		config.course = Course.objects.get(pk=request.POST['course_id'])
		config.config = json.dumps({'value' : request.POST['conf']})
		config.save()
	
	return redirect('/config/'+str(request.POST['game_id'])+'/'+str(request.POST['course_id'])+'?validate=1')