from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView, CreateView
from constance import config
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from main.models import Ad, Tag, Seller
from main.forms import UserForm


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


class SellerUpdateView(LoginRequiredMixin, UpdateView):
    model = Seller
    template_name = "main/seller_update.html"
    fields = "__all__"
    success_url = reverse_lazy("seller-info")
    login_url = reverse_lazy("index")

    def get_object(self):
        seller = Seller.objects.get(user=self.request.user)
        return seller

    def get_context_data(self):
        context = super().get_context_data()
        context["user_form"] = UserForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        self.object = form.save()
        user_form = UserForm(self.request.POST, instance=self.request.user)
        if user_form.is_valid():
            user_form.save()
        return super().form_valid(form)


class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    template_name = "main/create_ad.html"
    success_url = reverse_lazy("index")
    fields = "__all__"
    login_url = reverse_lazy("index")


class AdUpdateView(LoginRequiredMixin, UpdateView):
    model = Ad
    template_name = "main/update_ad.html"
    success_url = reverse_lazy("index")
    fields = "__all__"
    login_url = reverse_lazy("index")
    