from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from django.template.response import TemplateResponse
from constance import config
from django.contrib.auth.models import User

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
    template_name = "main/seller_update.html"

    def get_object(self):
        return Seller.objects.all()

    def get_context_data(self, request):
        context = {
            "user_form": UserForm(),
            "seller_form": SellerForm(),
        }

        return TemplateResponse(request, "main/seller_update.html", context)


# class SellerUpdateView(UpdateView):
#     template_name = "main/seller_update.html"
#     fields = '__all__'

#     def get_object(self):
#         if self.request.method == "POST":
#             user_form = UserForm(self.request.POST)
#             seller_form = SellerForm(self.request.POST)
#             if user_form.is_valid() and seller_form.is_valid():
#                 user_form.save()
#                 seller_form.save()
#                 return HttpResponseRedirect("seller-info")
#         else:
#             context = {
#                 "user_form": UserForm,
#                 "seller_form": SellerForm()
#             }
        
#         return TemplateResponse(self.request, "main/seller_update.html", context)


class SellerUpdateView(UpdateView):
    model = Seller
    template_name = "main/seller_update.html"
    fields = "__all__"

    def get_object(self):
        seller = Seller.objects.get(user=self.request.user)
        return seller

    def get_context_data(self):
        context = super().get_context_data()
        context["user_form"] = UserForm(instance=self.request.user)
        return context






        