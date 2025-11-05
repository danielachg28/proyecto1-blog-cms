#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "blog.settings.dev"
    )  # para usar entorno local por defecto
    try:
        from django.core.management import (  # noqa: PLC0415
            execute_from_command_line,
        )  # pyright: ignore[reportMissingImports]s  # noqa: E261, I001, PLC0415
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
