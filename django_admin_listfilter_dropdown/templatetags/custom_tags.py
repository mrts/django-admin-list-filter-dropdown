from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_setting(value, default=None):
    return getattr(settings, value, default)
