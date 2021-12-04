from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView, CreateView, TemplateView
from constance import config
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from main.models import Ad, Tag, Seller
from main.forms import UserForm, AdForm, ImageFormset


class IndexTemplateView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["title"] = "Главная страница"
        context["turn_on_block"] = config.MAINTENANCE_MODE
        return context


class AdListView(ListView):
    model = Ad
    paginate_by = 5

    def get_queryset(self):
        tag = self.request.GET.get("tag")
        if tag:
            queryset = Ad.objects.filter(tag__name=tag)
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
    login_url = "/accounts/login/"

    def get_object(self):
        seller = Seller.objects.get(user=self.request.user)
        return seller

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_form"] = UserForm(instance=self.object.user)
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
    login_url = "/accounts/login/"

    def get_context_data(self):
        context = super().get_context_data()
        context["picture_form"] = ImageFormset()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()  # Создается объект из основной формы
            formset = ImageFormset(request.POST, request.FILES, instance=self.object)
            if formset.is_valid():
                formset.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return form.invalid()


class AdUpdateView(LoginRequiredMixin, UpdateView):
    model = Ad
    template_name = "main/update_ad.html"
    success_url = reverse_lazy("index")
    fields = "__all__"
    login_url = "/accounts/login/"

    def get_context_data(self):
        context = super().get_context_data()
        context["picture_form"] = ImageFormset(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = self.get_object()
        formset = ImageFormset(request.POST, request.FILES, instance=self.object)
        if form.is_valid():
            form.save()
            if formset.is_valid():
                formset.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return form.invalid()
