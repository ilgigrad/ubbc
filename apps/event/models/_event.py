import uuid

from core.utils import SPORTS, random_color
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logo = models.ImageField(upload_to="logo/", blank=True, null=True)
    name = models.CharField(
        max_length=50,
        verbose_name=_("name"),
    )
    description = models.TextField(
        max_length=1000, verbose_name=_("description"), blank=True
    )
    language = models.CharField(
        default="en",
        max_length=10,
        choices=settings.LANGUAGE_CODES,
        verbose_name=_("prefered language"),
    )
    website = models.URLField(verbose_name=_("website"), blank=True, null=True)
    email = models.EmailField(verbose_name=_("email"), blank=True, null=True)
    telephone = PhoneNumberField(verbose_name=_("telephone"), blank=True, null=True)
    zip_code = models.CharField(max_length=10, verbose_name=_("zip code"), blank=True)
    city = models.CharField(max_length=50, verbose_name=_("city"), blank=True)
    country = CountryField(verbose_name=_("country"))
    sports = MultiSelectField(
        choices=SPORTS, default=[], blank=True, null=True, verbose_name=_("sports")
    )
    color = models.CharField(
        max_length=7, verbose_name=_("color"), blank=True, default=random_color
    )

    created_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("date create")
    )

    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("date update")
    )

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")
        get_latest_by = "created_at"
        ordering = ["-created_at"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        self.city = self.city.lower().strip()
        self.website = self.website.lower().strip()
        self.email = self.email.lower().strip()
        super().save(*args, **kwargs)
