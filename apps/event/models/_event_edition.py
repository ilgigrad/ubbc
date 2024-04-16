import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from ._event import Event


def get_year():
    if timezone.now().date().month > 7:
        return timezone.now().date().year + 1
    return timezone.now().date().year


class Edition(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("event"),
        related_name="editions",
    )

    date = models.DateField(blank=True, null=True, verbose_name=_("date"))
    year = models.IntegerField(
        default=get_year,
        verbose_name=_("year"),
    )

    created_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("date create")
    )

    updated_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("date update")
    )

    class Meta:
        verbose_name = _("edition")
        verbose_name_plural = _("editions")
        get_latest_by = "created_at"
        ordering = ["-created_at"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
