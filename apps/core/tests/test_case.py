from core.factories import UserFactory
from django.test import TestCase as DjangoTestCase
from django.utils import translation


class TestCase(DjangoTestCase):
    def setUp(self):
        translation.activate("en")
        super().setUp()

    def tearDown(self):
        UserFactory.reset_sequence()
