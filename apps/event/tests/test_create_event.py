from core.factories import EventFactory
from core.tests import TestCase


class TestEvent(TestCase):
    def test_createsEvent(self):
        event = EventFactory()

        self.assertEqual(event.name, event.name.lower())
