from django.shortcuts import render, redirect

TEMPLATES_PATH = 'game/'


def see(request):
    return render(request, TEMPLATES_PATH + 'game.html', {})