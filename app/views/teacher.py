from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse

def test(request):
	return render(request, '../templates/teacher/test.html', {})

def see(request):
	return render(request , '../templates/teacher/auth.html', {})

def auth(request):
	user = authenticate(username='john', password='secret')
	return HttpResponse(request.POST['email'])
	#return render(request , '../templates/teacher/auth.html', {})