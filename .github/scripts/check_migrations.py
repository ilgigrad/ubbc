import os
import sys
from subprocess import PIPE, run


def main():
    result = run(
        "python3 manage.py makemigrations",
        check=True,
        shell=True,
        stdout=PIPE,
        env={
            "DJANGO_SETTINGS_MODULE": "ubbc.test_settings",
            "PATH": os.environ.get("PATH"),
        },
    )

    if result.stdout != b"No changes detected\n":
        print("You forgot to commit your migrations!")
        sys.exit(1)


if __name__ == "__main__":
    main()
