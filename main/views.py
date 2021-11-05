from django.core.paginator import Paginator
from django.shortcuts import render
from constance import config
from django.utils.regex_helper import get_quantifier
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView

from main.models import Ad, Tag, Seller


def index(request):
    context = {
        "title": "Главная страница",
        "turn_on_block": config.MAINTENANCE_MODE,
    }
    
    return render(request, "main/index.html", context)


class AdListView(ListView):
    model = Ad
    paginate_by = 5

    def get_queryset(self):
        tag = self.request.GET.get("tag")
        if tag:
            queryset = Ad.objects.filter(tag__name = tag)
        else:
            queryset = super().get_queryset()
        
        return queryset
    
    extra_context = {
        "tags": Tag.objects.all(),
        "tag_name": ...
    }

class AdDetailView(DetailView):
    model = Ad
    template_name = "main/ad_detail.html"
    slug_field = "id"


class SellerUpdateView(UpdateView):
    ...