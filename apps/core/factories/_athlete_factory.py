from athlete.models import Athlete
from factory import PostGeneration, SubFactory
from factory.django import DjangoModelFactory

from ._user_factory import force_login


class AthleteFactory(DjangoModelFactory):
    class Meta:
        model = Athlete

    user = SubFactory("core.factories.UserFactory")
    club = "charenton"

    logged_in_to = PostGeneration(force_login)
