from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from app.models import Course, UserCourse, Profil
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from io import StringIO
from django.http import JsonResponse
import csv



TEMPLATES_PATH = 'score/'


def store(request, user_id, game_id):
	userToAddScore = UserCourse.objects.get(user_id=user_id)
	gamePlayed = Game.objects.get(pk=game_id)


	newScore = Score()

	newScore.game =  gamePlayed
	newScore.user = userToAddScore.user
	newScore.value = request.POST['score']
	newScore.save()

	return JsonResponse({'status':'OK'})
