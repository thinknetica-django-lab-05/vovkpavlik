from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import AdViewSet


router = DefaultRouter()
router.register(r'ads', AdViewSet, basename="ads")

urlpatterns = router.urls
