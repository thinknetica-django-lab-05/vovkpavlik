from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import AdViewSet, CategoryViewSet, SellerViewSet, AdPictureViewSet


router = DefaultRouter()
router.register(r'sellers', SellerViewSet, basename='sellers')
router.register(r'ads', AdViewSet, basename='ads')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'adpictures', AdPictureViewSet, basename='adpictures')

urlpatterns = router.urls
