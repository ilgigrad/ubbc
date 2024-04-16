from datetime import date

from core.utils import get_category
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Athlete(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="athlete",
        verbose_name=_("user"),
    )
    club = models.CharField(max_length=50, verbose_name=_("club"), blank=True)
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("date create")
    )

    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("date update")
    )

    class Meta:
        verbose_name = _("athlete")
        verbose_name_plural = _("athletes")
        get_latest_by = "created_at"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        self.club = self.club.lower().strip()
        super().save(*args, **kwargs)

    @property
    def category(self):
        return get_category(birth=birth_date.year, year=date.today().year)
