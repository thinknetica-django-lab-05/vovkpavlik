from django.urls import path

from main import views
from main.views import AdListView, AdDetailView, SellerUpdateView, AdCreateView, AdUpdateView


urlpatterns = [
    path('', views.index, name='index'),
    path('ads/', AdListView.as_view(), name='ad-list'),
    path('ads/add/', AdCreateView.as_view(), name='create-ad'),
    path('ads/<slug:slug>/', AdDetailView.as_view(), name='ad-detail'),
    path('ads/<slug:slug>/edit/', AdUpdateView.as_view(), name='update_ad'),
    path('accounts/seller/', SellerUpdateView.as_view(), name='seller-info'),
    
]