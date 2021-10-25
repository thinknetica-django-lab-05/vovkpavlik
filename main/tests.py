from django.test import TestCase

from django.contrib.auth.models import User
from main.models import Category, Ad, Seller, Tag


#Create users
users = ["guest_1", "guest_2", "guest_3"]
for user in users:
    User.objects.create_user(user, password=user)


#Create sellers
users = User.objects.all()

for user in users:
    Seller.objects.create(user=user)


#Create categories
categories = ["Антиквариат", "Музыкальное оборудование", "Одежда", "Копьютерная техника"]

for category in categories:
    Category.objects.create(title=category)


#Create ads
user_guest_1 = User.objects.get(username='guest_1')
user_guest_2 = User.objects.get(username='guest_2')
user_guest_3 = User.objects.get(username='guest_3')

seller_1 = Seller.objects.get(user=user_guest_1)
seller_2 = Seller.objects.get(user=user_guest_2)
seller_3 = Seller.objects.get(user=user_guest_3)

anticvar = Category.objects.get(title='Антиквариат')
music = Category.objects.get(title='Музыкальное оборудование')
clothes = Category.objects.get(title='Одежда')
comp = Category.objects.get(title='Копьютерная техника')

elephant_s_1 = Ad.objects.create(seller=seller_1, category=anticvar, title="Слоновый бивень", description="Большая слоновая кость")
piano_s_1 = Ad.objects.create(seller=seller_1, category=music, title="Старое фортепиано", description="Досталось от бабушки. Состояние - отличное")
gun_s_1 = Ad.objects.create(seller=seller_1, category=anticvar, title="Ружье 18 века", description="Не стреляет")

tag_anticvariat = Tag.objects.create(title="Антиквариат")
tag_exotic = Tag.objects.create(title="Экзотика")
tag_elephant_bone = Tag.objects.create(title="Слоновая кость")
tag_old = Tag.objects.create(title="Предметы старины")
tag_gun = Tag.objects.create(title="Оружие")
tag_music = Tag.objects.create(title="музыка")

elephant_s_1.tag.set([tag_anticvariat, tag_exotic, tag_elephant_bone])
piano_s_1.tag.set([tag_anticvariat, tag_old, tag_music])
tag_music = Tag.objects.create(title="музыка")





