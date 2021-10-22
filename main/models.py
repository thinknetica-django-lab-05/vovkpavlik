from django.db import models
from django.contrib.auth.models import User


class Seller(models.model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class Category(models.model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(prepopulate_from=('title',))


class Tag(models.model):
    pass


class Ads(models.model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
