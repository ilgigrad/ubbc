from core.utils import VOLUNTEER_ROLES
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Volunteer(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="volunteer",
        verbose_name=_("user"),
    )
    role = models.CharField(
        choices=VOLUNTEER_ROLES, max_length=50, verbose_name=_("role"), blank=True
    )
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("date create")
    )

    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("date update")
    )

    class Meta:
        verbose_name = _("volunteer")
        verbose_name_plural = _("volunteers")
        get_latest_by = "created_at"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        self.role = self.role.lower().strip()
        super().save(*args, **kwargs)
