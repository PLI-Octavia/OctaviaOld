from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from app.models import Course, UserCourse
from django.http import HttpResponse

TEMPLATES_PATH = 'student/'


def login_form(request):
    return render(request, TEMPLATES_PATH + 'login.html', {})


def auth(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    print(request.POST['username'], request.POST['password'])

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
    course = Course.objects.get(pk=request.POST['course'])
    

    user = User() 
    user.username = request.POST['name']
    user.set_password(request.POST['password'])
    user.first_name = "toto"
    user.last_name = "titi"
    user.email = "toto@gmail.fr"
    user.save()

    userCourse = UserCourse()
    userCourse.user = user
    userCourse.course = course
    userCourse.save()
    return HttpResponse('success')