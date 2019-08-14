"""
The DEFAULT configuration is loaded when the named _CONFIG dictionary
is not present in your settings.
"""
#######################
from __future__ import print_function, unicode_literals

from django.conf import settings

#######################

CONFIG_NAME = "STUDENTPERMS_CONFIG"  # must be uppercase!


DEFAULT = {
    # put application configuration items here.
}


#########################################################################


def get(setting):
    """
    get(setting) -> value

    setting should be a string representing the application settings to
    retrieve.

    The secondary setting name STUDENTPERMS_CONFIG_PROTECTED
    can be used to ensure that settings.py values will not be globbered
    by run-time configuration updates (e.g., from json files).
    (Especially useful for callable settings.)
    """
    assert setting in DEFAULT, "the setting %r has no default value" % setting
    app_settings = getattr(settings, CONFIG_NAME, DEFAULT)
    protected_name = CONFIG_NAME + "_PROTECTED"
    protected_settings = getattr(settings, protected_name, {})
    app_settings.update(protected_settings)
    return app_settings.get(setting, DEFAULT[setting])


def get_all():
    """
    Return all current settings as a dictionary.
    """
    app_settings = getattr(settings, CONFIG_NAME, DEFAULT)
    return dict(
        [(setting, app_settings.get(setting, DEFAULT[setting])) for setting in DEFAULT]
    )


#########################################################################
