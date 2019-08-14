"""
Admin classes for the  studentperms application
"""
#######################
from __future__ import print_function, unicode_literals

from functools import update_wrapper

from django.contrib import admin
from django.contrib.admin.views.autocomplete import AutocompleteJsonView
from django.contrib.admin.widgets import AutocompleteSelect
from django.db import models
from django.forms.widgets import CheckboxSelectMultiple
from django.urls import reverse
from people.admin import FlagFilterAutocompleteSelect

from .models import Permission, Reason, Student

#######################
#######################################################################


#######################################################################


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Students admin
    """

    search_fields = ["name", "student_number", "email"]


#######################################################################


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    """
    Reason admin
    """

    list_display = ["name", "ordering"]
    list_editable = ["ordering"]


#######################################################################


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    """
    Permission admin
    """

    autocomplete_fields = ["student", "section"]
    fieldsets = (
        (
            None,
            {
                "fields": [
                    "active",
                    "student",
                    "section",
                    "reasons",
                    "comments",
                    ("instructor", "instructor_signed"),
                    ("dept_head", "dept_head_signed"),
                ]
            },
        ),
    )
    formfield_overrides = {
        models.ManyToManyField: {"widget": CheckboxSelectMultiple},
        # models.ForeignKey: {'widget': InstructorAutocompleteSelect},
    }

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name in ["instructor", "dept_head"]:
            db = kwargs.get("using")
            kwargs["widget"] = FlagFilterAutocompleteSelect(
                db_field.remote_field, self.admin_site, using=db, flag="instructor"
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


#######################################################################
