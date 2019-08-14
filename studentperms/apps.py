#######################
from __future__ import print_function, unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

#######################
#########################################################################


#########################################################################


class StudentpermsConfig(AppConfig):
    name = "studentperms"
    verbose_name = _("Student permissions")

    def ready(self):
        """
        Any app specific startup code, e.g., registering signals,
        should go here.
        """


#########################################################################
