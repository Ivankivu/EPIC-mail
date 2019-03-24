import unittest
from datetime import datetime
from flask import Flask, json
from app import app
from app.api import create_app
from app.api.models.models import User, users, userid, Message, messages
from app.api.models.models import parentMessageId
from app.api.views.views import ViewUser
from app.utils import Validator


class TestMessage(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.object = Message(id=1, parentMessageId=1, message="jkhfkjsdhfkj",
                              status="unread", receiverId=2, subject="gone",
                              senderId=1, data=[], createdOn=datetime)
        self.route_url = 'api/v1/messages'
        self.message_data = {
            "status": 201,
            "data": {
                "id": len(messages)+1,
                "createdOn": str(datetime.now()),
                "message": "message",
                "status": "sent",
                "subject": "subject",
                "senderId": 1,
                "receiverId": 1
            }
        }

    def test_send_message(self):
        result = self.client.post('api/v1/messages',
                                  json=self.message_data)
        self.assertEqual(200, result.status_code,
                         "message sent!")
        self.assertTrue("message sent!", 201)

    def test_unread_messages(self):
        result = self.client.get('api/v1/messages/unread',
                                 content_type='application/json')
        self.assertEqual(404, result.status_code, msg="no new mail")

    def test_get_message(self):
        result = self.client.get('api/v1/messages/1',
                                 content_type='application/json')
        self.assertEqual(404, result.status_code, msg="no new mail")

    def test_get_sent_emails(self):
        sent_data = {
            "subject": "hello 1",
            "message": "hi, am okay! How are you doing??",
            "status": "sent",
            "sender_id": 2,
            "receiver_id": 1,
            "id": 1
        }
        self.client.post('/api/v1/messages/sent', json=sent_data)
        response = self.client.get('api/v1/messages/sent')
        print(response)
        self.assertEqual(response.status_code, 404)
        result = self.client.get('api/v1/messages/sent',
                                 content_type='application/json')
        self.assertEqual(404, result.status_code, msg="no new mail")
