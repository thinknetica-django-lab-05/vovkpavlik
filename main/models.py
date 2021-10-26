from django.db import models
from django.contrib.auth.models import User


"""Класс продавца. Вовзращает количество опубликованных объявлений"""
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    @property
    def get_count_adds(self):
        return 2


"""Класс категории. Возвращает название категории и слаг"""
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, allow_unicode=True)

    class Meta:
        verbose_name_plural = "Categories" 


"""Класс тэга. Возвращает название тэга"""
class Tag(models.Model):
    title = models.CharField(max_length=255)


"""Класс объявления. Возвращает название объявления, описание,
категорию и продавца, к которому относится объявление, и тэги
к этому объявлению + дата создания и изменения объявления"""
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
