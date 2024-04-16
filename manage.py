#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys


def main():
    argv = sys.argv

    if len(argv) > 1 and argv[1] == "install":
        from apps.core.management.commands._install import install

        install(argv[2:])
        exit(0)

    try:
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(argv)


if __name__ == "__main__":
    main()
