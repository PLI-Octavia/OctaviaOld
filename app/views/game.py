from django.shortcuts import render, redirect

TEMPLATES_PATH = 'game/'


def see(request):
    # TODO: Dynamize
    game = {"game_name": "Maths",
            "game_path": "maths"}
    return render(request, TEMPLATES_PATH + 'show.html', game)