from django.urls import path

from main import views
from main.views import AdListView, AdDetailView


urlpatterns = [
    path('', views.index, name='index'),
    path('ads/', AdListView.as_view(), name='ad-list'),
    path('ads/<slug:slug>/', AdDetailView.as_view(), name='ad-detail'),
    
]