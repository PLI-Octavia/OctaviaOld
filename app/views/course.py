from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from app.models import Course

TEMPLATES_PATH  =  '../templates/courses/'

def see(request):
	request.user
	myCourses = Course.objects.filter(user_id=request.user.id)
	return render(request, TEMPLATES_PATH + 'see.html', {'courses': myCourses})

def create(request):
	return render(request, TEMPLATES_PATH + 'create.html', {})

def store(request):
	#Create a new Course
	course = Course()
	#A course belong to a user
	course.user_id = request.user
	course.name = request.POST['name']
	course.save()
	#Redirect to the see view
	return redirect('courses')
