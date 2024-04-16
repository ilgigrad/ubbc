import os
import subprocess
import sys

from django.core.management.base import BaseCommand

DJANGO = ["manage.py", "runserver"]
WEBPACK = ["npm", "run", "dev-server"]

SHOW_OUTPUT = None


def get_output_type(dont_show_output):
    return subprocess.DEVNULL if dont_show_output else SHOW_OUTPUT


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument(
            "--no-django-stdout",
            action="store_true",
            help="Do not show django standard output.",
        )
        parser.add_argument(
            "--no-django-stderr",
            action="store_true",
            help="Do not show django error output.",
        )
        parser.add_argument(
            "--filter-logs",
            action="store_true",
            help="Filter some ajax update log messages.",
        )
        parser.add_argument(
            "--debugpy",
            help="Run django with debugpy on specified port.",
        )

    def handle(self, *args, **options):
        try:

            self._run_django(options)
        finally:
            pass

    def _run_django(self, options):
        env = os.environ.copy()
        if options["filter_logs"]:
            env["FILTER_LOGS"] = "True"

        if options["debugpy"]:
            extra = ["-m", "debugpy", "--listen", f"localhost:{options['debugpy']}"]
        else:
            extra = []

        # We need to run Django in a different thread because it will constantly
        # kill itself to reaload the configuration.
        subprocess.run(
            [sys.executable, *extra, *DJANGO],
            env=env,
            stdout=get_output_type(options["no_django_stdout"]),
            stderr=get_output_type(options["no_django_stderr"]),
        )
