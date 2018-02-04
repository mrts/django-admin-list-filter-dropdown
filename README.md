# django-admin-list-filter-dropdown

A Django admin filter implementation that renders as a dropdown.

If you have more than ten values for a field that you want to filter by in
Django admin, the filtering sidebar gets long, cluttered and hard to use.

This app contains the `DropdownFilter` class that renders as a drop-down in the
filtering sidebar to avoid this problem.

# Usage

Install:

```sh
pip install django-admin-list-filter-dropdown
```

Enable in `settings.py` before `django.contrib.admin`:

```py
INSTALLED_APPS = (
    ...
    'django_admin_listfilter_dropdown',
    'django.contrib.admin',
    '',
    ...
)

```

For `RelatedSelect2DropdownFilter` you need the following in your `ModelAdmin`:

```
class Media:
    """
    This is required for the batch update view to work with select2 dropdowns
    """
    js = (
        'admin/js/vendor/jquery/jquery.min.js',
        'admin/js/vendor/select2/select2.full.min.js',
        'admin/js/jquery.init.js',
        'django_admin_listfilter_dropdown/autocomplete.js',
    )

    css = {
        'screen': (
            'admin/css/vendor/select2/select2.min.css',
            'admin/css/autocomplete.css',
        ),
    }
```

Also make sure your `STATICFILES_FINDERS` setting is either set to the Django default or contains:

```
...
'django.contrib.staticfiles.finders.AppDirectoriesFinder',
```

Use in `admin.py`:

```py
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

class EntityAdmin(admin.ModelAdmin):
    ...
    list_filter = (
        # for ordinary fields
        ('a_charfield', DropdownFilter),
        # for related fields
        ('a_foreignkey_field', RelatedDropdownFilter),
        # RelatedSelect2DropdownFilter requires Django2 and the foreignkey field needs to be listed in the ModelAdmin's search_fields and autocomplete_fields 
        # https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.autocomplete_fields
        ('a_foreignkey_field2', RelatedSelect2DropdownFilter),
    )
```

# Example

Here's what it looks like:

![Screenshot of dropdown admin filter](https://raw.githubusercontent.com/mrts/django-admin-list-filter-dropdown/master/docs/list-filter-dropdown.png)

# Credits

Based on [this StackOverflow question](http://stackoverflow.com/a/20900314/258772) and
[code from FeinCMS](https://github.com/feincms/feincms/blob/master/feincms/templates/admin/filter.html).
