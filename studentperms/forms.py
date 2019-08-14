"""
Forms for the studentperms application.
"""
#######################
from __future__ import print_function, unicode_literals

from django import forms

from .models import StudentpermsModel

#######################
#######################################################################


#######################################################################


class StudentpermsModelForm(forms.ModelForm):
    """
    Form for the model.
    """

    class Meta:
        model = StudentpermsModel
        exclude = ["active"]
        # widgets = {
        #    }


#######################################################################
#######################################################################
#######################################################################
