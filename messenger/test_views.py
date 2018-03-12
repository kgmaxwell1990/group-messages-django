from django.test import TestCase
from .views import *
# from django.core.urlresolvers import resolve

class MessageViewsTests(TestCase):
    def test_inbox_template(self):
        response = self.client.get('/messenger/inbox/')
        self.assertTemplateUsed(response, 'messenger/inbox.html')
        
    def test_sent_template(self):
        response = self.client.get('/messenger/sent/')
        self.assertTemplateUsed(response, 'messenger/sent.html')
        
    def test_view_message_does_not_exist(self):
        response = self.client.get('/messenger/view_message/2/')
        self.assertEqual(response.status_code, 404)
    
    # def test_view_message_template(self):
    #     response = self.client.get('/messenger/view_message/2/')
    #     self.assertTemplateUsed(response, 'messenger/view_message.html')

    def test_compose_message_template(self):
        response = self.client.get('/messenger/compose_message/')
        self.assertTemplateUsed(response, 'messenger/compose_message.html')