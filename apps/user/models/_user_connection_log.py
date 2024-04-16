import uuid

from core.utils import get_session_cookie_age
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class ConnectionLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="connections",
        verbose_name=_("user"),
    )

    connected_at = models.DateTimeField(
        default=timezone.now, verbose_name=_("connection date")
    )

    ip_address = models.GenericIPAddressField(
        protocol="both", unpack_ipv4=True, null=True
    )
    session = models.ForeignKey(
        Session,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        unique_together = (("user", "connected_at"),)
        verbose_name = _("user connection log")
        verbose_name_plural = _("users connections logs")
        get_latest_by = "connected_at"
        ordering = ["-connected_at"]

    @property
    def expire_date(self):
        if self.session:
            return self.session.expire_date

    @property
    def elapsed(self):
        if self.session:
            return int(
                (
                    timezone.now() + get_session_cookie_age() - self.expire_date
                ).total_seconds()
            )
