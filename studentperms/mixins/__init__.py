"""
Reusable library of mixins.
"""
#######################
from __future__ import print_function, unicode_literals

from .admin_autocomplete import LabelAutocompleteJsonView
from .cbv_admin import AdminFormMixin, AdminSiteViewMixin, ClassBasedViewsAdminMixin
from .default_filter_admin import DefaultFilterMixin
from .exact_search_admin import SearchResultsAdminMixin
from .formset import UpdateWithFormsetMixin
from .restricted_forms import (
    RestrictedAdminMixin,
    RestrictedFormViewMixin,
    RestrictedQuerysetMixin,
)
from .single_fk import SingleFKAdminMixin, SingleFKFormViewMixin

#######################


__all__ = [
    "LabelAutocompleteJsonView",
    "ClassBasedViewsAdminMixin",
    "AdminSiteViewMixin",
    "AdminFormMixin",
    "DefaultFilterMixin",
    "SearchResultsAdminMixin",
    "UpdateWithFormsetMixin",
    "RestrictedAdminMixin",
    "RestrictedFormViewMixin",
    "RestrictedQuerysetMixin",
    "SingleFKAdminMixin",
    "SingleFKFormViewMixin",
]
