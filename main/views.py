from django.shortcuts import render
from constance import config
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from main.models import Ad


def index(request):
    context = {
        "title": "Главная страница",
        "turn_on_block": config.MAINTENANCE_MODE,
    }
    
    return render(request, 'main/index.html', context)


class AdListView(ListView):
    model = Ad


class AdDetailView(DetailView):
    model = Ad
    template_name = 'main/ad_detail.html'
    slug_field = 'id'
