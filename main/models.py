from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    """Класс продавца. Вовзращает количество опубликованных объявлений"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    @property
    def get_count_adds(self):
        return 2


class Category(models.Model):
    """Класс категории. Возвращает название категории и слаг"""
    title = models.CharField(
        max_length=255,
        help_text="Название категории"    
    )
    slug = models.SlugField(
        max_length=255, 
        allow_unicode=True,
        help_text="slug формируется автоматически"
        )

    class Meta:
        verbose_name_plural = "Categories" 


class Tag(models.Model):
    """Класс тэга. Возвращает название тэга"""
    title = models.CharField(max_length=255)


class Ad(models.Model):
    """Класс объявления. Возвращает название объявления, описание,
категорию и продавца, к которому относится объявление, и тэги
к этому объявлению + дата создания и изменения объявления"""
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link = models.ManyToManyField(Tag)


    def __str__(self):
        return self.title
