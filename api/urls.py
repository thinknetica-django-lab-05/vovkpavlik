from django.urls import path

from .views import AdListView


urlpatterns = [
    path('ads/', AdListView.as_view()),
]
