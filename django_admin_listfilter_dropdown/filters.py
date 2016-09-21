from django.contrib.admin.filters import AllValuesFieldListFilter, RelatedFieldListFilter

class DropdownFilter(AllValuesFieldListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'

class RelatedDropdownFilter(RelatedFieldListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'
