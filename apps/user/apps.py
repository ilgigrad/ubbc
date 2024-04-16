from django.apps import AppConfig


class UserConfig(AppConfig):
    name = "user"

    def ready(self):
        __import__(self.name + ".receivers")

        # Overwrite standard Django Anonymoususer
        from django.contrib.auth import models as auth_models
        from user.models import AnonymousUser

        auth_models.AnonymousUser = AnonymousUser
