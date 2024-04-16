from datetime import date, timedelta

from django.db.models.signals import post_save
from factory.django import DjangoModelFactory, mute_signals
from user.models import UserProfile


@mute_signals(post_save)
class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = UserProfile

    accept_privacy = True
    accept_user_tos = True
    birth_date = date.today() - timedelta(days=365.24 * 35)
    gender = "F"
    telephone = "+33795412556"
    zip_code = "73100"
    city = "chambéry"
    country = "FR"
    language = "fr"
    nationality = "FR"
