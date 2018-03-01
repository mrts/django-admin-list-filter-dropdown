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


@register.simple_tag(takes_context=True)
def get_model(context):
    """
    RelatedFieldListFilter will provide the full info (__str__) of the instance
    however it becomes very slow once there are a cpl k instances in the db table
    it is much faster to look up the value here for the selected instance.
    :param context:
    :return:
    """
    spec = context.get('spec')
    model = spec.field.related_model
    if spec.lookup_val:
        return model.objects.get(pk=spec.lookup_val).__str__()
    return 'All'
