from django.test import TestCase

from django.contrib.auth.models import User
from .models import Category, Ad, Seller


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





