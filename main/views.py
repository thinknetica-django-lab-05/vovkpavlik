from typing import ClassVar
from django.shortcuts import render
from constance import config
from django.views.generic.list import ListView

from main.models import Ad


def index(request):
    username = request.user.username
    context = {
        "title": "Главная страница",
        "turn_on_block": config.MAINTENANCE_MODE,
        "username": username
    }
    
    return render(request, 'main/index.html', context)


class AdListView(ListView):
    model = Ad

    def get_products(self, **kwargs):
        context = super().get_products(**kwargs)
        return context


