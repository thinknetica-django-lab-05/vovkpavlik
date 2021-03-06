import random

from django.http import HttpResponseRedirect
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView, CreateView, TemplateView
from constance import config
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.urls import reverse_lazy, reverse

from main.models import Ad, User, Seller, Category, Subscription
from main.forms import UserForm, ImageFormset


class IndexTemplateView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["title"] = "Главная страница"
        context["turn_on_block"] = config.MAINTENANCE_MODE
        return context


# @method_decorator(cache_page(60 * 60), name='dispatch')
class AdListView(ListView):
    model = Ad
    ordering = ['-created_at']
    paginate_by = 5

    # def get_tags(self):
    #     all_tags = Ad.objects.all().values("tags")
    #     unique_tags = set()
    #     for tags in all_tags:
    #         unique_tags.update(tags['tags'])
    #     return unique_tags

    def check_active_subscription(self, user):
        subscription = Subscription.objects.get(user__username=user)
        category = Category.objects.get(name=self.request.GET.get("category"))
        return subscription.category.filter(name=category).exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.request.user

        # context["tags"] = self.get_tags
        context["banned_user"] = user.groups.filter(name="banned users")
        context["ads_unique_categories"] = Ad.objects.all().distinct("category")
        if self.request.GET.get("category"):
            context["active_subscription"] = self.check_active_subscription(user)
            context["choosen_category_name"] = self.request.GET.get("category")
        return context

    def get_queryset(self):
        # tag = self.request.GET.get("tag")
        category_name = self.request.GET.get("category")
        seller_name = self.request.GET.get("seller")
        query_search = self.request.GET.get("query_search")
        if category_name:
            queryset = Ad.objects.filter(category__name=category_name)
        elif seller_name:
            queryset = Ad.objects.filter(seller__user__username=seller_name)
        elif query_search:
            queryset = Ad.objects.annotate(
                search=SearchVector('name', 'description'),
            ).filter(search=SearchQuery(query_search))
        else:
            queryset = super().get_queryset()
        return queryset

    def post(self, request):
        category_name = request.GET.get("category")
        user = User.objects.get(username=request.user)
        if request.POST:
            subscription, create = Subscription.objects.get_or_create(user=user)
            subscription.category.add(Category.objects.get(name=category_name))
            return HttpResponseRedirect(f"{self.request.path_info}?category={category_name}")


class AdDetailView(DetailView):
    model = Ad
    template_name = "main/ad_detail.html"
    slug_field = "id"

    def get_context_data(self, **kwargs):
        if not cache.get("dynamic_price"):
            cache.set(
                "dynamic_price",
                round(self.object.price * random.uniform(0.8, 1.2)),
                60
            )
        context = super().get_context_data()
        context["dynamic_price"] = cache.get("dynamic_price")
        context["ads"] = Ad.objects.all().order_by("-created_at")[:5]
        return context


class SellerUpdateView(LoginRequiredMixin, UpdateView):
    model = Seller
    template_name = "main/seller_update.html"
    # fields = "__all__"
    fields = ("itn", "avatar", "phone")
    success_url = reverse_lazy("seller-info")
    login_url = "/accounts/login/"

    def get_object(self, queryset=None):
        seller, created = Seller.objects.get_or_create(user=self.request.user)
        return seller

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_form"] = UserForm(instance=self.object.user)
        context["subscription"] = Subscription.objects.get(user__username=self.object.user)
        return context

    def post(self, request, *args, **kwargs):
        subscription = Subscription.objects.get(user__username=self.request.user)
        self.object = self.get_object()
        form = self.get_form()
        user_form = UserForm(self.request.POST, instance=self.request.user)

        if "subscription" in request.POST:
            category = Category.objects.get(name=request.POST.get('subscription'))
            subscription.category.remove(category)
            return HttpResponseRedirect(self.request.path_info)

        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            return super().form_valid(form)
        return super().form_invalid(form)


class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    template_name = "main/create_ad.html"
    fields = ("name", "description", "category", "tags", "price")
    login_url = "/accounts/login/"

    def get_context_data(self):
        context = super().get_context_data()
        context["picture_form"] = ImageFormset()
        context["user"] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            # Создается объект из основной формы
            self.object = form.save(commit=False)
            self.object.seller = self.request.user.seller
            self.object.save()
            formset = ImageFormset(
                request.POST,
                request.FILES,
                instance=self.object
            )
            if formset.is_valid():
                formset.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return form.invalid()

    def get_success_url(self):
        return reverse_lazy("ad-detail", args=(self.object.id,))


class AdUpdateView(LoginRequiredMixin, UpdateView):
    model = Ad
    template_name = "main/update_ad.html"
    fields = ("name", "description", "category", "tags", "price")
    login_url = "/accounts/login/"

    def get_context_data(self):
        context = super().get_context_data()
        context["picture_form"] = ImageFormset(instance=self.object)
        context["seller"] = self.object.seller
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset = ImageFormset(
            request.POST,
            request.FILES,
            instance=self.object
        )
        if form.is_valid():
            form.save()
            if formset.is_valid():
                formset.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return form.invalid()

    def get_success_url(self):
        return reverse_lazy("ad-detail", args=(self.object.id,))
