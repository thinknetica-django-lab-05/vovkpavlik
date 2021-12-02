from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver


from pytils import translit

from main.validator import validate_itn
from main.new_ads_message import send_new_ads_message


class BaseModel(models.Model):
    name = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    itn = models.CharField(
        "ИНН", max_length=11,
        default="000000000",
        validators=[validate_itn]
    )
    avatar = models.ImageField(upload_to="images/avatars/", default="images/avatars/default-avatar.jpg")

    @property
    def get_count_adds(self):
        filtered_seller = Ad.objects.filter(seller=self)
        adds_num = filtered_seller.count()

        return adds_num

    def __str__(self):
        return self.user.username


class Category(BaseModel):
    slug = models.SlugField(max_length=255, allow_unicode=True)

    def save(self, *args, **kwargs):
        category_name = self.name
        self.slug = translit.slugify(u'' + category_name)

        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"


class Tag(BaseModel):
    ...


class Ad(BaseModel):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name="Продавец")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    description = models.TextField("Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag, verbose_name="Тэги")
    price = models.PositiveIntegerField("Цена", default=0)
    is_archive = models.BooleanField("Продано", null=True)


class ArchiveManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_archive=True)


class ArchiveAds(Ad):
    objects = ArchiveManager()

    class Meta:
        proxy = True


class AdPicture(BaseModel):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление")
    image = models.ImageField(upload_to="images/ads/", default="images/ads/default-product.jpg")


class Subscription(models.Model):
    user = models.ManyToManyField(User)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name="common users"))


# send_new_ads_message()
