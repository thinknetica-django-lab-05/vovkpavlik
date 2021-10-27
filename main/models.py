from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract=True
    

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    @property
    def get_count_adds(self):
        filtered_seller = Ad.objects.filter(seller=self)
        adds_num = filtered_seller.count()
        
        return adds_num


class Category(BaseModel):
    slug = models.SlugField(max_length=255, allow_unicode=True)

    class Meta:
        verbose_name_plural = "Categories" 


class Tag(BaseModel):
    pass


class Ad(BaseModel):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag)
    price = models.PositiveIntegerField(default=0)


class ArchiveManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset()


class ArchiveAds(Ad):

    objects = ArchiveManager()

    class Meta:
        proxy = True



