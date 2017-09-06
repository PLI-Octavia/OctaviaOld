from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from app.models import Course, UserCourse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from io import StringIO
import csv

TEMPLATES_PATH = 'student/'


def login_form(request):
    return render(request, TEMPLATES_PATH + 'login.html', {})


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        # Next one who redirect to a nonexistent template gets to be assfucked by the entire seven nation army.
        # return redirect('student_home') <- fuck you
        return HttpResponse('success')
    else:
        return HttpResponse('failed')
        # TODO error handling like teacher


@login_required
def home(request):
    return render(request, TEMPLATES_PATH + 'home.html', {})

@login_required
def create(request, course_id):
	myCourses = UserCourse.objects.filter(user=request.user)
	return render(request, TEMPLATES_PATH + 'create.html', {'courses': myCourses, 'course_id': course_id})

@login_required
def store(request):
    course = Course.objects.get(pk=request.POST['course'])
    
    user = User()
    user.username = request.POST['name']
    user.set_password(request.POST['password'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = "toto@gmail.fr"
    user.save()

    userCourse = UserCourse()
    userCourse.user = user
    userCourse.course = course
    userCourse.save()

    return redirect('/course/'+str(course.id)+'/edit/')

def storeCSV(request):
    file = request.FILES['students']
    csvf = StringIO(file.read().decode())
    reader = csv.reader(csvf, delimiter=',')
    # user = User()
    # course = Course.objects.get(pk=request.POST['course'])

    # I am not ashamed :D
    for row in reader:
        user = User()
        user.username = row[0]
        user.set_password(row[1])
        user.first_name = row[2]
        user.last_name = row[3]
        user.email = "toto@gmail.fr"
        user.save()
        course = Course.objects.get(pk=request.POST['course'])
        userCourse = UserCourse()
        userCourse.user = user
        userCourse.course = course
        userCourse.save()

    return redirect('/course/')
