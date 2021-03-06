from django.urls import path

from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap

from main.views import IndexTemplateView
from main.views import AdListView, AdDetailView, SellerUpdateView
from main.views import AdCreateView, AdUpdateView

from main.sitemaps import AdSitemap


sitemaps = {
    'blog': AdSitemap
}


urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('robots.txt/', TemplateView.as_view(template_name="main/robots.txt", content_type="text/plain")),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('ads/', AdListView.as_view(
        template_name='main/ad_list.html'),
         name='ad-list'
         ),
    path('ads/add/', AdCreateView.as_view(), name='create-ad'),
    path('ads/<slug:slug>/', AdDetailView.as_view(), name='ad-detail'),
    path('ads/<int:pk>/edit/', AdUpdateView.as_view(), name='update_ad'),
    path('accounts/seller/', SellerUpdateView.as_view(), name='seller-info'),
]
