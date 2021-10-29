from django.shortcuts import render
from constance import config


def index(request):
    username = request.user.username
    context = {
        "title": "Главная страница",
        "turn_on_block": config.MAINTENANCE_MODE,
        "username": username
    }
    
    return render(request, 'main/index.html', context)
