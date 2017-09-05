from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from app.models import Course, UserCourse
from django.http import HttpResponse

TEMPLATES_PATH = 'student/'


def login_form(request):
    return render(request, TEMPLATES_PATH + 'login.html', {})


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        # Next one who redirect to a nonexistent template gets to be ass fucked by the entire seven nation army.
        # return redirect('student_home') <- fuck you
        return HttpResponse('success')
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

    return redirect('/course/'+str(course.id)+'/edit/')
    # return render(request, '/course/1/edit/', {})
    # return HttpResponse('success')