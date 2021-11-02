
from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
@stringfilter
def invert_string(phrase):
    return (''.join(reversed(phrase)))
