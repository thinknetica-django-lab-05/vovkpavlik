from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)


class Tag(models.Model):
    title = models.CharField(max_length=255)


class Ad(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link = models.ManyToManyField(Tag)


    def __str__(self):
        return self.title
