"""
Models for the studentperms application.
"""
#######################################################################
from __future__ import print_function, unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible

from .querysets import PermissionQuerySet, ReasonQuerySet, StudentQuerySet

#######################################################################
#######################################################################
#######################################################################


class StudentPermsBaseModel(models.Model):
    """
    An abstract base class.
    """

    active = models.BooleanField(default=True)
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="creation time"
    )
    modified = models.DateTimeField(
        auto_now=True, editable=False, verbose_name="last modification time"
    )

    class Meta:
        abstract = True


#######################################################################
#######################################################################
#######################################################################


@python_2_unicode_compatible
class Student(StudentPermsBaseModel):
    """
    A description of this model.
    """

    name = models.CharField(max_length=100)
    student_number = models.CharField(max_length=32)
    email = models.EmailField(blank=True)

    objects = StudentQuerySet().as_manager()

    class Meta:
        base_manager_name = "objects"

    def __str__(self):
        s = self.name + " [{}]".format(self.student_number)
        if self.email:
            s += " <{}>".format(self.email)
        return s


#######################################################################


@python_2_unicode_compatible
class Reason(StudentPermsBaseModel):
    """
    A description of this model.
    """

    name = models.CharField(
        max_length=100, help_text="A reason for the special permission"
    )
    ordering = models.PositiveSmallIntegerField(
        default=50,
        help_text="Reasons are sorted by the ordering number first, then by name",
    )

    objects = ReasonQuerySet().as_manager()

    class Meta:
        base_manager_name = "objects"
        ordering = ["ordering", "name"]

    def __str__(self):
        return self.name


#######################################################################


@python_2_unicode_compatible
class Permission(StudentPermsBaseModel):
    """
    A description of this model.
    """

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    section = models.ForeignKey("classes.Section", on_delete=models.PROTECT)
    reasons = models.ManyToManyField(Reason, help_text="Select as many as apply")
    comments = models.TextField(
        help_text="Justification.  Include both sections here for a section change."
    )
    instructor = models.ForeignKey(
        "people.Person",
        limit_choices_to={"flags__slug": "instructor"},
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="permissions_granted_as_instructor",
    )
    instructor_signed = models.DateField(
        blank=True,
        null=True,
        verbose_name="signed on",
        help_text="Dates are YYYY-MM-DD.",
    )
    dept_head = models.ForeignKey(
        "people.Person",
        verbose_name="department head or designate",
        limit_choices_to={"flags__slug": "instructor"},
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="permissions_granted_as_head",
    )
    dept_head_signed = models.DateField(
        blank=True,
        null=True,
        verbose_name="signed on",
        help_text="Dates are YYYY-MM-DD.",
    )

    objects = PermissionQuerySet().as_manager()

    class Meta:
        base_manager_name = "objects"

    def __str__(self):
        return "{} – {} ({})".format(self.student, self.section, self.section.term)

    def has_instructor_signed(self):
        return (self.instructor is not None) and (self.instructor_signed is not None)

    def has_dept_head_signed(self):
        return (self.dept_head is not None) and (self.dept_head_signed is not None)

    def is_complete(self):
        return self.has_instructor_signed() and self.has_dept_head_signed()


#######################################################################
#######################################################################
#######################################################################
