from django.urls import path
from . import views

from main.views import IndexTemplateView
from main.views import AdListView, AdDetailView, SellerUpdateView
from main.views import AdCreateView, AdUpdateView


urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('ads/', AdListView.as_view(
        template_name='main/ad_list.html'),
         name='ad-list'
         ),
    path('ads/add/', AdCreateView.as_view(), name='create-ad'),
    path('ads/<slug:slug>/', AdDetailView.as_view(), name='ad-detail'),
    path('ads/<int:pk>/edit/', AdUpdateView.as_view(), name='update_ad'),
    path('accounts/seller/', SellerUpdateView.as_view(), name='seller-info'),
    path('chat/', views.chat_page, name='chat_page'),
    path('chat/<str:room_name>/', views.room, name='room')

]
