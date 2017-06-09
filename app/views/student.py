from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse

TEMPLATES_PATH = '../templates/student_auth/'


def login_form(request):
    return render(request, TEMPLATES_PATH + 'login.html', {})


def auth(request):
    user = authenticate(username=request.POST['email'] + '@student', password=request.POST['password'])

    if user is not None:
        login(request, user)
        return redirect('student_home')
    else:
        return HttpResponse('failed')
        # TODO error handling like teacher

# TODO make this logged-in only
def home(request):
    return render(request, TEMPLATES_PATH + 'home.html', {})
