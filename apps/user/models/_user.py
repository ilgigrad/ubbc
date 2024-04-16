import uuid

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(_("email address"), unique=True, null=True)
    first_name = models.CharField(_("first name"), unique=False, max_length=100)
    last_name = models.CharField(_("last name"), unique=False, max_length=100)
    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("update date")
    )
    password = models.CharField(_("password"), max_length=128, blank=True)
    password_updated_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("password update date")
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._password = self.password

    @property
    def full_name(self):
        if self.first_name:
            return " ".join([self.first_name.capitalize(), self.last_name.capitalize()])
        else:
            return " ".join(
                [
                    x.capitalize()
                    for x in (self.email.split("@")[0])
                    .replace("_", ".")
                    .replace("-", ".")
                    .split(".")
                ]
            )

    def __str__(self):
        return f"{self.full_name}|{self.email}"

    @property
    def login_name(self):
        if self.first_name:
            return self.first_name.capitalize()
        return self.email

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        self.email = BaseUserManager.normalize_email(self.email)
        self.first_name = self.first_name.lower().strip()
        self.last_name = self.last_name.lower().strip()
        if self._password != self.password:
            self.password_updated_at = timezone.now()
        super().save(*args, **kwargs)

    @property
    def is_organizer(self):
        return hasattr(self, "organizer")

    @property
    def is_volunteer(self):
        return hasattr(self, "volunteer")

    @property
    def is_athlete(self):
        return hasattr(self, "athlete")
