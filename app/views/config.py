from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
import json
import pprint

from app.models import Course, Game, GameCourse , User, GameConfig

TEMPLATES_PATH = 'config/'

@login_required
def see(request, game_id, course_id):
	game = Game.objects.get(pk=game_id)
	cur = GameConfig.objects.filter(course_id=course_id, game_id=game_id).first()

	metaJson = '{}' if not game.config else game.config
	configJson = cur.config if cur and cur.config else '{}'

	return render(request, TEMPLATES_PATH + 'see.html', {'course_id': course_id, 'game_id':game_id, 'metadata': metaJson, 'config': configJson})

def store(request):
	game = Game.objects.get(pk=request.POST['game_id'])
	
	config = GameConfig.objects.filter(course_id=request.POST['course_id'], game_id=request.POST['game_id']).first()
	if not config:
		config = GameConfig()
		config.game = game
		config.course = Course.objects.get(pk=request.POST['course_id'])
	config.config = request.POST['conf']
	config.save()
	
	return redirect('/config/'+str(request.POST['game_id'])+'/'+str(request.POST['course_id'])+'?validate=1')
