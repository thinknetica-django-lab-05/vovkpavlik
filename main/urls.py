from django.urls import path

from main import views
from main.views import AdListView


urlpatterns = [
    path('', views.index, name='index'),
    path('ads/', AdListView.as_view(), name='ad-list'),
]