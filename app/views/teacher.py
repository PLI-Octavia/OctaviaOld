from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse

TEMPLATES_PATH  =  '../templates/teacher/'

def see(request):
	return render(request , TEMPLATES_PATH + 'auth.html', {})

def auth(request):
	user = authenticate(username=request.POST['email'], password=request.POST['password'])
	
	if user is not None :
		#login is a auth method to set user in session
		login(request, user)
		return redirect('teacher_home')
	else :
		return HttpResponse('failed')
	#TODO => redirect to auth view with bootstrap alert to say auth don t pass

def home(request):
	return render(request , TEMPLATES_PATH + 'home.html', {})

def logout(request):
	return render(request , TEMPLATES_PATH + 'auth.html', {})	