import unittest
from datetime import datetime
from flask import Flask, json
from app import app
from app.api import create_app
from app.api.models.models import User, users, userid, Message, messages
from app.api.models.models import parentMessageId
from app.api.views.views import ViewUser
from app.utils import Validator


class TestUser(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.object = User(userid=1, firstname='ivan', lastname='ivan',
                           email='ivan@gmail.com',
                           password='gates')
        self.route_url = 'api/v1/users'
        self.new_user = dict(
            userid=userid,
            username="ivan",
            email="ivan@example.com",
            password="andela14"
        )

    def test_instantiation(self):
        self.assertIsInstance(self.object, User)

    def test_user_exists(self):
        user = User(userid=1, firstname='ivan', lastname='ivan',
                    email='ivan@gmail.com', password="andela14")
        self.assertTrue(user)

    def test_add_user(self):
        result = self.client.post('api/v1/users',
                                  content_type='application/json',
                                  data=json.dumps(self.object.__dict__)
                                  )
        self.assertIsNot(405, result.status_code,
                         "Account was created successfully!")
        self.assertTrue("Account was created successfully!", 201)

    def test_getting_user_users(self):
        result = self.client.get('api/v1/users',
                                 content_type='application/json')
        self.assertEqual(200, result.status_code, msg="found users")


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

    def test_unread_messages(self):
        result = self.client.get('api/v1/messages/unread',
                                 content_type='application/json')
        self.assertEqual(200, result.status_code, msg="no new mail")
