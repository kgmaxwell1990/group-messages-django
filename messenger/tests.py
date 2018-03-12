from django.test import TestCase
from .views import *
from django.core.urlresolvers import resolve

class MessengerAppTests(TestCase):
    def test_inbox_page_resolves(self):
        inbox_page = resolve("/messenger/inbox/")
        self.assertEqual(inbox_page.func, get_inbox)

    def test_sent_page_resolves(self):
        sent_page = resolve("/messenger/sent/")
        self.assertEqual(sent_page.func, sent)

    def test_view_message_page_resolves(self):
        view_message_page = resolve("/messenger/view_message/3")
        self.assertEqual(view_message_page.func, view_message)
        
    def test_message_requires_id(self):
        response = self.client.get("/messenger/view_message/")
        self.assertEqual(response.status_code, 404)
        
    def test_compose_message_page_resolves(self):
        compose_message_page = resolve("/messenger/compose_message/")
        self.assertEqual(compose_message_page.func, compose_message)
