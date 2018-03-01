(function (jQuery) {
    var init = function ($element, options) {
        var settings = jQuery.extend({
            ajax: {
                data: function (params) {
                    return {
                        term: params.term,
                        page: params.page
                    };
                }
            }
        }, options);
        $element.select2(settings).on('change', function (ev) {
            var filter_param = jQuery(this).data('lookup-kwarg');
            // TODO: Not all browsers support URLSearchParams
            // https://caniuse.com/#search=URLSearchParams
            params = new URLSearchParams(window.location.search);
            if (jQuery(this).val()) {
                params.set(filter_param, jQuery(this).val());
            } else {
                params.delete(filter_param);
            }
            window.location.search = params.toString();
        })
    };

    jQuery.fn.djangoAdminFilterSelect2 = function (options) {
        var settings = jQuery.extend({}, options);
        jQuery.each(this, function (i, element) {
            var $element = jQuery(element);
            init($element, settings);
        });
        return this;
    };

    jQuery(function () {
        jQuery('.admin-filter-autocomplete').djangoAdminFilterSelect2();
    });

}(django.jQuery));
