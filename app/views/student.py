from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from app.models import Course, UserCourse
from django.http import HttpResponse

TEMPLATES_PATH = 'student/'
OCTAVIA_STUDENT_EMAIL = '@student.octavia.fr'


def login_form(request):
    return render(request, TEMPLATES_PATH + 'login.html', {})


def auth(request):
    user = authenticate(username=request.POST['email'] + OCTAVIA_STUDENT_EMAIL, password=request.POST['password'])

    if user is not None:
        login(request, user)
        return redirect('student_home')
    else:
        return HttpResponse('failed')
        # TODO error handling like teacher


# TODO make this logged-in only
def home(request):
    return render(request, TEMPLATES_PATH + 'home.html', {})

def create(request):
	myCourses = UserCourse.objects.filter(user=request.user)
	return render(request, TEMPLATES_PATH + 'create.html', {'courses': myCourses})

def store(request):
	return render(request, TEMPLATES_PATH + 'login.html', {})