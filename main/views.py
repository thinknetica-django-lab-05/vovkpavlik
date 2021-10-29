from django.shortcuts import render
from constance import config


def index(request):
    context = {
        "title": "Главная страница",
        "turn_on_block": config.MAINTENANCE_MODE
    }
    return render(request, 'main/index.html', context)
