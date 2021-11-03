from django.shortcuts import render
from constance import config
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from main.models import Ad, Tag


def index(request):
    context = {
        "title": "Главная страница",
        "turn_on_block": config.MAINTENANCE_MODE,
    }
    
    return render(request, "main/index.html", context)


class AdListView(ListView):
    model = Ad

    extra_context = {
        "tags": Tag.objects.all(),
        }

    def get_queryset(self):
        tag = self.request.GET.get("tag")
        if tag:
            queryset = Ad.objects.filter(tag__name = tag)
        else:
            queryset = super().get_queryset()
        print(type(self.request.GET.get("tag")))
        
        return queryset
    

class AdDetailView(DetailView):
    model = Ad
    template_name = "main/ad_detail.html"
    slug_field = "id"

