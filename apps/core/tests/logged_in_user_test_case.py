from core.factories import AthleteFactory, EventOrganizerFactory, VolunteerFactory
from core.tests.test_case import TestCase


class LoggedInAthleteTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.athlete = AthleteFactory()
        self.client.force_login(self.athlete.user)


class LoggedInOrganizerTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.organizer = EventOrganizerFactory()
        self.client.force_login(self.organizer.user)


class LoggedInVolunteerTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.volunteer = VolunteerFactory()
        self.client.force_login(self.volunteer.user)
