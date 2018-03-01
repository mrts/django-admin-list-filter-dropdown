from django.contrib.admin.filters import (
    AllValuesFieldListFilter,
    ChoicesFieldListFilter,
    RelatedFieldListFilter, RelatedOnlyFieldListFilter
)


class DropdownFilter(AllValuesFieldListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'


class ChoiceDropdownFilter(ChoicesFieldListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'


class RelatedDropdownFilter(RelatedFieldListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'


class RelatedOnlyDropdownFilter(RelatedOnlyFieldListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'


class RelatedSelect2DropdownFilter(RelatedOnlyFieldListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_select2_filter.html'
