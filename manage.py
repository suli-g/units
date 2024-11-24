#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import sys
from dotenv import load_dotenv


def main():
    """
    Loads environment variables from a .env file in this project's route
    directory.

    Environment Variables:
        SECRET_KEY: The value to use for this Django project's SECRET_KEY.
        DJANGO_SETTINGS_MODULE: The module path to this project's settings module.
    """
    # Add support for reading from the .env file.
    load_dotenv()
    """Run administrative tasks."""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
