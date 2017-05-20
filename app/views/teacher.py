from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse

def see(request):
	return render(request , '../templates/teacher/auth.html', {})

def auth(request):
	user = authenticate(username=request.POST['email'], password=request.POST['password'])
	
	if user is not None :
		login(request, user)
		return redirect('home_teacher')
	else :
		return HttpResponse('failed')
	#return render(request , '../templates/teacher/auth.html', {})

def home(request):
	return render(request , '../templates/teacher/home.html', {})

def logout(request):
	return render(request , '../templates/teacher/auth.html', {})	