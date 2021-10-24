from django.test import TestCase

from django.contrib.auth.models import User
from .models import Category, Ad, Seller


#Create users
users = ["guest_1", "guest_2", "guest_3"]
for user in users:
    User.objects.create_user(user, password=user)


#Create sellers
from main.models import Seller
users = User.objects.all()

for user in users:
    Seller.objects.create(user=user)



