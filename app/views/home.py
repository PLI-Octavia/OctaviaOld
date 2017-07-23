from django.shortcuts import render, redirect
from django.http import HttpResponse

TEMPLATES_PATH = 'home/'

def see(request):
    return render(request, TEMPLATES_PATH + 'see.html', {})