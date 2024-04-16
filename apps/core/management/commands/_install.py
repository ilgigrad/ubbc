import argparse
import subprocess
import sys


def install(argv):
    """
    We want to run install before we have Django installed so we
    have to run the install command manually without Django.
    """

    command = Command()

    parser = argparse.ArgumentParser()
    command.add_arguments(parser)
    args = parser.parse_args(argv)

    command.handle(**vars(args))


def run(command, **kwargs):
    return subprocess.run(command.split(" "), check=True, **kwargs)


class Command:
    def add_arguments(self, parser):
        parser.add_argument(
            "--reinstall",
            action="store_true",
            help="Remove installation and start clean.",
        )

    def handle(self, *args, **options):
        if options["reinstall"]:
            self._clean_pip()

        self._install_requirements()

    def _clean_pip(self):
        installed_packages = run(f"{self._get_pip()} freeze", capture_output=True)
        run(f"xargs {self._get_pip()} uninstall -y", input=installed_packages.stdout)

    def _install_requirements(self):
        run(f"{self._get_pip()} install -r requirements.txt")

    def _get_pip(self):
        python = sys.executable

        if self._is_system_python(python):
            print("Please use a virtual environment like pyvenv or pipenv")
            print("and not your system python installation!")
            exit(1)
        return f"{sys.executable} -m pip"

    def _is_system_python(self, python):
        return self._get_base_prefix_compat() == sys.prefix

    def _get_base_prefix_compat(self):
        return (
            getattr(sys, "base_prefix", None)
            or getattr(sys, "real_prefix", None)
            or sys.prefix
        )
