from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from app.models import Course, UserCourse, Profil
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
        userCourse = UserCourse.objects.get(user_id=user.id)
        return redirect('/course/'+str(userCourse.course_id)+'/game?student=1')
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

    profil = Profil()
    profil.user = user
    profil.role = 0
    profil.save()

    userCourse = UserCourse()
    userCourse.user = user
    userCourse.course = course
    userCourse.save()

    return redirect('/course/'+str(course.id)+'/edit/')

@login_required
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

@login_required
def update(request, user_id, course_id):
    userToUpdate = User.objects.get(pk=user_id)
    return render(request, TEMPLATES_PATH + 'update.html', {'user': userToUpdate, 'course_id': course_id})

@login_required
def save(request):
    userToUpdate = User.objects.get(pk=request.POST['user_id'])
    userToUpdate.username = request.POST['name']
    userToUpdate.first_name = request.POST['first_name']
    userToUpdate.last_name = request.POST['last_name']    
    userToUpdate.save()
    return redirect('/course/'+str(request.POST['course'])+'/edit/')   

@login_required
def delete(request, user_id, course_id):
    userToDelete = User.objects.get(pk=user_id)
    userToDelete.delete()
    return redirect('/course/'+str(course_id)+'/edit/')    





