import os
import subprocess
import sys
import time

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--only_py",
            action="store_true",
            help="Only run python tests.",
        )

        parser.add_argument(
            "--pytest",
            action="store_true",
            help="Use pytest instead of djangotest.",
        )
        parser.add_argument(
            "--coverage",
            action="store_true",
            help="Collect test coverage data.",
        )
        parser.add_argument(
            "--sequential",
            action="store_true",
            help="Run tests one after another.",
        )
        parser.add_argument(
            "--functional", action="store_true", help="Run all functional tests."
        )
        parser.add_argument(
            "--show", action="store_true", help="Show browser for functional tests."
        )

    def handle(self, *args, **options):
        try:
            start = time.time()

            if options["functional"]:
                self._run_functional_tests(options)
            else:
                self._run_python_unit_tests(options)

            end = time.time()

            print("\n\033[32;1mOK", end=" ")
            self._print_elapsed_time(start, end)
            sys.exit(0)

        except subprocess.CalledProcessError:
            pass
        print("\n\033[31;1mFAIL")

    def _print_elapsed_time(self, start, end):
        elapsed = round(end - start, 2)
        print(f"(needed {elapsed} seconds)")

    def _run_python_unit_tests(self, options):
        folder = "apps"
        settings = "test_settings"

        if options["pytest"]:
            self._run_pytest(options, folder=folder, settings=settings)
        else:
            self._run_django_test(options, folder=folder, settings=settings)

    def _run_functional_tests(self, options):
        folder = "functional_tests"
        settings = "functional_test_settings"

        if options["pytest"]:
            self._run_pytest(options, folder=folder, settings=settings)
        else:
            self._run_django_test(options, folder=folder, settings=settings)

    def _run_pytest(self, options, *, folder, settings):
        command = [sys.executable, "-m", "pytest", folder]

        if not options["sequential"]:
            command += ["-n", "auto"]

        if options["coverage"]:
            command += ["--cov=."]
        env = {
            **os.environ.copy(),
            "DJANGO_SETTINGS_MODULE": "ubbc." + settings,
            "SHOW": str(options["show"]),
        }

        subprocess.run(command, env=env, check=True)

    def _run_django_test(self, options, *, folder, settings):
        command = [sys.executable, "manage.py", "test", folder]

        if not options["sequential"]:
            command += ["--parallel"]

        if options["coverage"]:
            command = command[:1] + ["-m", "coverage", "run"] + command[1:]

        env = {
            **os.environ.copy(),
            "DJANGO_SETTINGS_MODULE": "ubbc." + settings,
            "SHOW": str(options["show"]),
        }

        subprocess.run(command, env=env, check=True)
