from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage


class FlatPageAdmin(admin.ModelAdmin):
    content = forms.CharField(widget=CKEditorWidget())


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
