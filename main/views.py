from django.shortcuts import render
from constance import config
from main.models import Ad


def index(request):
    username = request.user.username
    context = {
        "title": "Главная страница",
        "turn_on_block": config.MAINTENANCE_MODE,
        "username": username
    }
    
    return render(request, 'main/index.html', context)


def ad_list(request):
    context = {
        "products": Ad.objects.all()
    }

    return render(request, 'main/ad_list.html', context)
