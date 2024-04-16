import uuid

from core.utils import ORGANIZER_ROLES
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from ._event import Event


class Organizer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="organizer",
        verbose_name=_("user"),
    )
    role = models.CharField(
        choices=ORGANIZER_ROLES, max_length=20, verbose_name=_("role"), blank=True
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("event"),
        related_name="organizers",
    )
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("date create")
    )

    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("date update")
    )

    class Meta:
        verbose_name = _("organizer")
        verbose_name_plural = _("organizers")
        get_latest_by = "created_at"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        self.role = self.role.lower().strip()
        super().save(*args, **kwargs)
