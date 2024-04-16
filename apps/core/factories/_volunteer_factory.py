from factory import PostGeneration, SubFactory
from factory.django import DjangoModelFactory
from volunteer.models import Volunteer

from ._user_factory import force_login


class VolunteerFactory(DjangoModelFactory):
    class Meta:
        model = Volunteer

    user = SubFactory("core.factories.UserFactory")

    logged_in_to = PostGeneration(force_login)

    role = "aid"
