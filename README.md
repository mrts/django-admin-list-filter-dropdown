# django-admin-list-filter-dropdown

A Django admin filter implementation that renders as a dropdown.

If you have more than ten values for a field that you want to filter by in
Django admin, the filtering sidebar gets long, cluttered and hard to use.

This app contains the `DropdownFilter` class that renders as a drop-down in the
filtering sidebar to avoid this problem.

**P.S.** It will only render the dropdown if the field has 4 or more choices,
if you have fewer choices it will render the normal filtering list.

# Usage

Install:

```sh
pip install django-admin-list-filter-dropdown
```

Enable in `settings.py`:

```py
INSTALLED_APPS = (
    ...
    'django_admin_listfilter_dropdown',
    ...
)

```

Use in `admin.py`:

```py
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

class EntityAdmin(admin.ModelAdmin):
    ...
    list_filter = (
        # for ordinary fields
        ('a_charfield', DropdownFilter),
        # for choice fields
        ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('a_foreignkey_field', RelatedDropdownFilter),
    )
```

Example of a custom filter that uses the provided template:

```py
class CustomFilter(SimpleListFilter):
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'

    def lookups(self, request, model_admin):
        ...

    def queryset(self, request, queryset):
        ...
```

# Example

Here's what it looks like:

![Screenshot of dropdown admin filter](https://raw.githubusercontent.com/mrts/django-admin-list-filter-dropdown/master/docs/list-filter-dropdown.png)

# Credits

Based on [this StackOverflow question](http://stackoverflow.com/a/20900314/258772) and
[code from FeinCMS](https://github.com/feincms/feincms/blob/master/feincms/templates/admin/filter.html).
