from django.test import TestCase
from .models import Message
# from django.core.urlresolvers import resolve

class MessageModelsTests(TestCase):
    def test_str_works(self):
        message = Message()
        message.subject = "Test Subject"
        self.assertEqual("Test Subject", str(message))