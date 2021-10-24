from django.test import TestCase

from django.contrib.auth.models import User
from .models import Category, Ad, Seller


#Create sellers
from django.contrib.auth.models import User
from main.models import Seller
users = User.objects.all()

for user in users:
    Seller.objects.create(user=user)



