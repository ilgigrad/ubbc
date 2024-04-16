from django.db.models.signals import post_save
from factory import PostGeneration, RelatedFactory, Sequence
from factory.django import DjangoModelFactory, mute_signals
from user.models import User


def force_login(user, _, client):
    if client:
        client.force_login(user)


def set_password(user, _, password):
    user.set_password(password if password else "password")


@mute_signals(post_save)
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    email = Sequence(lambda n: f"user{n}@spotl.io")
    first_name = "FirstName"
    last_name = "LastName"
    password = PostGeneration(set_password)
    is_superuser = False

    profile = RelatedFactory(
        "core.factories.UserProfileFactory", factory_related_name="user"
    )

    logged_in_to = PostGeneration(force_login)


class AthleteUserFactory(UserFactory):
    member = RelatedFactory(
        "core.factories.AthleteFactory", factory_related_name="user"
    )


class VolunteerUserFactory(UserFactory):
    member = RelatedFactory(
        "core.factories.VolunteerFactory", factory_related_name="user"
    )


class OrganizerUserFactory(UserFactory):
    posteditor = RelatedFactory(
        "core.factories.EventOrganizerFactory", factory_related_name="user"
    )


class SuperUserFactory(UserFactory):
    is_staff = True
    is_superuser = True
