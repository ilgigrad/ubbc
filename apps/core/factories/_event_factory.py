from event.models import Event
from factory.django import DjangoModelFactory


# Don't use, use FixedFolderFactory instead
class EventFactory(DjangoModelFactory):
    class Meta:
        model = Event

    # Should not be item
    name = "ubbc"
    description = "une course rapide"
    language = "en"
    website = "http://ubbc.fr"
    email = "contact@ubbc.fr"
    telephone = "+695411221"
    zip_code = "75019"
    city = "paris"
    country = "FR"
    sports = "trail"
