from django.contrib.admin.filters import AllValuesFieldListFilter, RelatedFieldListFilter, ChoicesFieldListFilter

class DropdownFilter(AllValuesFieldListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'

class ChoiceDropdownFilter(ChoicesFieldListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'

class RelatedDropdownFilter(RelatedFieldListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'
