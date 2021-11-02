from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('ads/', views.ad_list, name='ad_list')
]