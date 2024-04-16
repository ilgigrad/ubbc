# pylint: disable=unused-argument

from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone
from user.models import User, UserConnectionLog, UserProfile


def login_handler(sender, user, request, **kwargs):
    ip = request.META.get("REMOTE_ADDR", None)
    UserConnectionLog.objects.create(
        user=user, ip_address=ip, session_id=request.session.session_key
    )
    user.profile.last_connection = timezone.now()
    user.profile.save()


user_logged_in.connect(login_handler)


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(pre_delete, sender=UserProfile)
def auto_delete_avatar_on_delete(sender, instance, **kwargs):
    if instance.avatar:
        instance.avatar.delete()
