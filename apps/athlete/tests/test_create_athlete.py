from athlete.models import Athlete
from core.factories import AthleteFactory
from core.tests import TestCase


class TestAtlete(TestCase):
    def test_createsAthlete(self):
        user = AthleteFactory().user

        athlete = Athlete.objects.get(user__email=user.email)
        self.assertEqual(athlete.club, athlete.club.lower())
