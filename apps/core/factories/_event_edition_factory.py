from datetime import date, timedelta

from event.models import EventEdition
from factory import PostGeneration, SubFactory
from factory.django import DjangoModelFactory

from ._user_factory import force_login


class EditionFactory(DjangoModelFactory):
    class Meta:
        model = EventEdition

    year = (date.today() + timedelta(days=185)).year
    date = date.today() + timedelta(days=185)
    event = SubFactory("core.factories.EventFactory")

    logged_in_to = PostGeneration(force_login)
