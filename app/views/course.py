from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from app.models import Course, UserCourse

TEMPLATES_PATH = '../templates/courses/'


def see(request):
    myCourses = UserCourse.objects.filter(user=request.user, active=1)

    return render(request, TEMPLATES_PATH + 'see.html', {'courses': myCourses})

def create(request):
    return render(request, TEMPLATES_PATH + 'create.html', {})

@login_required
def store(request):
    # Create a new Course
    course = Course()
    course.name = request.POST['name']
    course.save()

    # A course belong to a user
    userCourse = UserCourse()
    userCourse.course = course
    userCourse.user = request.user
    userCourse.save()

    # Redirect to the see view
    return redirect('courses')

@login_required
def edit(request, course_id):
    request.session['course_id'] = course_id
    users = UserCourse.objects.filter(course=course_id)
    courseToSee = Course.objects.get(pk=course_id)
    request.session['course_name'] = courseToSee.name 
    return render(request, TEMPLATES_PATH + 'edit.html', {'users': users, 'course_id': course_id, 'course':courseToSee})

@login_required
def param(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, TEMPLATES_PATH + 'param.html', {'course': course})

#Hide course
@login_required
def delete(request, course_id):
    courseToHide = UserCourse.objects.get(pk=course_id)
    courseToHide.active = 0
    courseToHide.save()
    return redirect('courses')

#Update Course information
@login_required
def update(request):
    course = Course.objects.get(pk=request.POST['course_id'])
    course.name = request.POST['name']
    course.save()
    return redirect('/course/' + str(request.POST['course_id']) + '/edit/')
