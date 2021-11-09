from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from django.template.response import TemplateResponse
from constance import config
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from main.models import Ad, Tag, Seller
from main.forms import UserForm, SellerForm


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
    }


class AdDetailView(DetailView):
    model = Ad
    template_name = "main/ad_detail.html"
    slug_field = "id"


class SellerUpdateView(UpdateView):
    # UpdateView работает с формами, и в модели Seller форма уже есть.
    model = Seller
    template_name = "main/seller_update.html"
    fields = "__all__"
    success_url = reverse_lazy("seller-info")   # При удачной валидации - переходим на главную страницу

# Чтобы загрузить форму на страницу, нужно использовать пк или слаг.
# Или сразу получить конкретный объект, в данном случае - юзера.
    def get_object(self):
        seller = Seller.objects.get(user=self.request.user)
        return seller


# Так как UpdateView по дефолту работает только с одной моделью,
# То небходимо вручную добавить еще одну модель и форму к ней.
    def get_context_data(self):
        # Здесь я вызываю метод, который дает словарь
        context = super().get_context_data()
        
        # И в словарь я добавляю ключ со значением - форма.
        # Так как использовать другую модель я не могу, я получаю данные по связанной модели.
        context["user_form"] = UserForm(instance=self.request.user) # из инстанса берем данные
        return context

    def form_valid(self, form):
        self.object = form.save()
        user_form = UserForm(self.request.POST, instance=self.request.user)
        if user_form.is_valid():
            user_form.save()
        return super().form_valid(form)

