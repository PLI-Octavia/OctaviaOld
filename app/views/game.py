from django.shortcuts import render, redirect
from app.models import Game

TEMPLATES_PATH = 'game/'


def see(request, game_id):
    game = Game.objects.get(pk=game_id)

    # Game folder name in static/games must be the game name.
    return render(request, TEMPLATES_PATH + 'show.html', {"game_name": game.name})