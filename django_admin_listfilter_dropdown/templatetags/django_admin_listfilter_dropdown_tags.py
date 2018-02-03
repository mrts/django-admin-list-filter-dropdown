from django.urls import reverse
from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def get_autocomplete_url(context):
    spec = context.get('spec')
    app_label = spec.field.related_model._meta.app_label
    model_name = spec.field.related_model._meta.model_name

    return reverse('admin:{}_{}_autocomplete'.format(
        app_label,
        model_name,
    ))
