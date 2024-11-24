"""
The main URL resolver for the Units project.

Implements a path which takes the user to the default
Django admin site.
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
