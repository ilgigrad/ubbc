from core.factories import EventEditionFactory, EventFactory
from core.tests import TestCase


class TestEdition(TestCase):
    def test_createsEvent(self):
        event = EventFactory()
        edition = EventEditionFactory(event=event)

        self.assertEqual(edition.date.year, edition.year)
