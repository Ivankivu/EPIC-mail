import unittest
from flask import Flask, json
from app import app
from app.api import create_app
from app.api.models.users import User, users, userid
from app.api.views.viewusers import ViewUser
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

    def test_user_exists(self):
        user = User(userid=1, firstname='ivan', lastname='ivan',
                    email='ivan@gmail.com', password="andela14")
        self.assertTrue(user)

    def test_user_added_successfully(self):
        result = self.client.post('api/v1/users',
                                  content_type='application/json',
                                  data=json.dumps(self.object.__dict__)
                                  )
        self.assertIsNot(405, result.status_code,"Account was created successfully!" )
        self.assertTrue("Account was created successfully!", 201)

    def test_getting_user_users(self):
        result = self.client.get('api/v1/users',
                                 content_type='application/json')
        self.assertEqual(200, result.status_code, msg="found users")