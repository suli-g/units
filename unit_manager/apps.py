"""
Configuration for the `unit_manager` application.

This module defines the configuration for the `unit_manager` app,
allowing Django to identify and initialize it properly.

Classes:
    UnitManagerConfig: Configures the `unit_manager` application.
"""

from django.apps import AppConfig


class UnitManagerConfig(AppConfig):
    """
    Configures the `unit_manager` application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "unit_manager"
