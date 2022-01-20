from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy

from main.models import Ad


class AdSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Ad.objects.all()

    def location(self, obj):
        return reverse_lazy("ad-detail", args=(obj.id,))
