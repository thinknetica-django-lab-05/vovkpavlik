from django.urls import path

from main import views
from main.views import AdListView, AdDetailView, SellerUpdateView, AdCreateView


urlpatterns = [
    path('', views.index, name='index'),
    path('ads/', AdListView.as_view(), name='ad-list'),
    path('ads/add/', AdCreateView.as_view(), name='create-ad'),
    path('ads/<slug:slug>/', AdDetailView.as_view(), name='ad-detail'),
    path('accounts/seller/', SellerUpdateView.as_view(), name='seller-info'),
    
]