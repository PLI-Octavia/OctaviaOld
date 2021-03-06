from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.models import User
from django.http import HttpResponse

import pprint

TEMPLATES_PATH = 'teacher/'


def see(request):
    return render(request, TEMPLATES_PATH + 'auth.html', {})


def auth(request):
    user = authenticate(username=request.POST['email'], password=request.POST['password'])

    if user is not None:
        # login is a auth method to set user in session
        login(request, user)
        return redirect('courses')
    else:
        return HttpResponse('failed')
    # TODO => redirect to auth view with bootstrap alert to say auth don t pass


def home(request):
    return render(request, TEMPLATES_PATH + 'home.html', {})


def logout(request):
    if 'course_id' in request.session:
        del request.session['course_id']
        del request.session['course_name']
    django_logout(request)
    return redirect('home')

def store(request):
    return render(request, TEMPLATES_PATH + 'auth.html', {})

    
