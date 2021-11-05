import random

from django import template

register = template.Library()

@register.simple_tag
def get_count():
    return random.randrange(1, 30)
