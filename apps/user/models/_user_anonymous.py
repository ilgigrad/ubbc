from django.contrib.auth.models import AnonymousUser as DjangoAnonymousUser


class AnonymousUser(DjangoAnonymousUser):
    @property
    def is_organizer(self):
        return False

    @property
    def is_athlete(self):
        return False

    @property
    def is_volunteer(self):
        return False
