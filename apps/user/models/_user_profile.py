from core.utils import GENDERS, random_color
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    """
    Profile's class extends User's class with some informations that are not linked to auth management.
    """

    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="profile",
        verbose_name=_("user"),
    )

    color = models.CharField(
        max_length=7, verbose_name=_("color"), blank=True, default=random_color
    )

    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)
    accept_privacy = models.BooleanField(
        default=False, verbose_name=_("accept privacy terms")
    )
    accept_user_tos = models.BooleanField(
        default=False, verbose_name=_("accept user terms of service")
    )
    language = models.CharField(
        default="fr",
        max_length=10,
        choices=settings.LANGUAGES,
        verbose_name=_("prefered language"),
    )

    nationality = CountryField(
        verbose_name=_("nationality"), default="FR", blank=True, null=True
    )
    birth_date = models.DateField(blank=True, null=True, verbose_name=_("birth date"))
    gender = models.CharField(
        null=True,
        blank=True,
        max_length=1,
        choices=GENDERS,
        verbose_name=_("gender"),
    )
    telephone = PhoneNumberField(verbose_name=_("telephone"), blank=True, null=True)
    zip_code = models.CharField(max_length=10, verbose_name=_("zip code"), blank=True)
    city = models.CharField(max_length=50, verbose_name=_("city"), blank=True)
    country = CountryField(verbose_name=_("country"))

    created_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("date create")
    )

    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("date update")
    )

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
        get_latest_by = "created_at"
        ordering = ["-created_at"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._avatar = self.avatar

    def __str__(self):
        return f"{self.user}|{self.gender}|{self.nationality} "

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        self.city = self.city.lower().strip()
        super().save(*args, **kwargs)

        if self._avatar != self.avatar:  # test if the avatar has changed
            self._avatar.delete()  # delete the original avatar
        self._avatar = self.avatar

    @property
    def has_optin(self, *args, **kwargs):
        return self.privacy and self.user_tos

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
