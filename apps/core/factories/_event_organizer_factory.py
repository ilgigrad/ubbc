from event.models import EventOrganizer
from factory import PostGeneration, SubFactory
from factory.django import DjangoModelFactory

from ._user_factory import force_login


class OrganizerFactory(DjangoModelFactory):
    class Meta:
        model = EventOrganizer

    role = "admin"

    user = SubFactory("core.factories.UserFactory")
    event = SubFactory("core.factories.EventFactory")

    logged_in_to = PostGeneration(force_login)
