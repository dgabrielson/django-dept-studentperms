# Core idea from https://www.netlandish.com/blog/2017/09/19/simple-trick-improve-django-admin-search-results/
# Generalized by Dave Gabrielson.

import operator
from functools import reduce

from django.db.models import Case, IntegerField, Q, Value, When


class SearchResultsAdminMixin(object):
    """
    Classes using this mixin need to supply an ``exact_search_boost_fields``
    attribute which is a list of fields to test for exact matches
    (in priority sequence).
    """

    def get_search_results(self, request, queryset, search_term):
        """ Show exact match for title and slug at top of admin search results.
        """
        if not hasattr(self, "exact_search_boost_fields"):
            raise ImproperlyConfigured(
                "No exact search boost fields.  Provide a "
                "exact_search_boost_fields attribute on the ModelAdmin."
            )

        qs, use_distinct = super(SearchResultsAdminMixin, self).get_search_results(
            request, queryset, search_term
        )

        search_term = search_term.strip()
        if not search_term:
            return qs, use_distinct

        def cond_int(query):
            return Case(
                When(query, then=Value(1)),
                default=Value(0),
                output_field=IntegerField(),
            )

        # Construct annotations...
        annotations = {
            "exact_{}".format(f): cond_int(Q(**{"{}__iexact".format(f): search_term}))
            for f in self.exact_search_boost_fields
        }
        qs = qs.annotate(**annotations)

        order_by = []
        for f in self.exact_search_boost_fields:
            if qs.filter(**{"exact_{}".format(f): 1}).exists():
                order_by.append("-exact_{}".format(f))

        if order_by:
            qs = qs.order_by(*order_by)

        return qs, use_distinct
