import random

from django import template

register = template.Library()

def get_notifications_num():
    random_num = random.randrange(1, 30)
