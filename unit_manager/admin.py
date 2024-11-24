"""
Registers the Unit model in the admin site.
"""
from django.contrib import admin
from unit_manager.models import Unit

admin.site.register(Unit)
