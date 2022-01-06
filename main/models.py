import random
from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver

from pytils import translit

from main.validator import validate_itn


def get_random_code():
    random_code = random.randint(1000, 9999)
    return str(random_code)


class BaseModel(models.Model):
    name = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Seller(models.Model):
    """
        Модель продавца.
        Имеет привязку к пользователю через поле `OneToOne`.
        Возвращает ИНН, аватарку и номер телефона.
        Подсчитывает количество созданных объявлений для продавца
        через декоратор `@property`.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    itn = models.CharField(
        "ИНН", max_length=11,
        default="000000000",
        validators=[validate_itn]
    )
    avatar = models.ImageField(
        upload_to="images/avatars/",
        default="images/avatars/default-avatar.jpg"
    )
    phone = models.CharField(
        max_length=12,
        blank=True,
        help_text="Номер телефона пользователя"
    )

    @property
    def get_count_adds(self):
        filtered_seller = Ad.objects.filter(seller=self)
        adds_num = filtered_seller.count()

        return adds_num

    def __str__(self):
        return self.user.username


class Category(BaseModel):
    """
        Модель категории.
        Наследуется от базовой модели `BaseModel`.
        Возвращает название категории и слаг.
        Переопределен метод `save` для перевода кирилицы
        в латиницу.
    """
    slug = models.SlugField(max_length=255, allow_unicode=True)

    def save(self, *args, **kwargs):
        category_name = self.name
        self.slug = translit.slugify(u'' + category_name)

        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"


class Tag(BaseModel):
    """
        Модель тэга.
        Наследуется от базовой модели `BaseModel`.
        Возвращает название тэга.
    """
    ...


class Ad(BaseModel):
    """
        Модель объявления.
        Связана с моделью продавца и моделью категории
        полем `Foreignkey`.
        Возвращает продавца, категорию, описание, дату создания
        и дату редактирования, тэги, цену и статус объявления -
        архивное или действительное.

    """
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        verbose_name="Продавец"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )
    description = models.TextField("Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
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
    """
        Модель изображения для объявлений.
        Связана с моделью объявления.
        Возвращает связанное объявление и изображение.
    """
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        verbose_name="Объявление"
    )
    image = models.ImageField(
        upload_to="images/ads/",
        default="images/ads/default-product.jpg"
    )


class Subscription(models.Model):
    """
        Модель подписчика.
        Связана с моделью пользователя.
        Пользователю, который подписан на объявления,
        приходят ежедневные сообщения о новых поступлениях.
    """
    user = models.ManyToManyField(User)


class SMSLog(models.Model):
    """
        Модель для подтверждения телефона.
        Связана с моделью продавца полем `OneToOne`.
        Возвращает продавца, сгенерированный 4-х значный код подтверждения,
        ответ от провайдера - сервиса Twilio и статус пользователя - подтвержден
        номер или нет.
    """
    seller = models.OneToOneField(Seller, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=4, default=get_random_code)
    confirmed = models.BooleanField("Номер подтвержден", null=True)
    response = models.TextField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name="common users"))
