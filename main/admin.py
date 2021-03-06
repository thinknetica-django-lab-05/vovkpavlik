from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.contrib.flatpages.models import FlatPage

from .models import Seller, Category, Ad, ArchiveAds
from .models import AdPicture, Subscription


@admin.action(description="Добавить объявления в архив")
def make_archived(modeladmin, request, queryset):
    queryset.update(is_archive=True)


class FlatPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FlatPage
        fields = "__all__"


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatPageAdminForm


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ["user", "get_count_adds"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "seller",
        "category",
        "name",
        "price",
        "created_at",
        "updated_at",
        "is_archive",
    ]
    list_filter = ["created_at", "tags"]
    actions = [make_archived]


@admin.register(AdPicture)
class AdPicture(admin.ModelAdmin):
    list_display = ["ad"]


admin.site.register(Subscription)
admin.site.register(ArchiveAds)
