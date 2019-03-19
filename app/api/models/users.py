import string
from flask import Flask, request, Response, jsonify
from app import app
from app.utils import Validator

users = {}


class User:

    def __init__(self, **kwargs):
        self.userid = kwargs.get("userid")
        self.email = kwargs.get("email")
        self.firstname = kwargs.get("username")
        self.lastname = kwargs.get("username")
        self.password = kwargs.get("password")

    def signup_user(self):
        data = request.get_json()
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        password = data["password"]

        add_user = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password": password
        }

        existing_user = [user for user in users if
                         user["email"] == email
                         ]
        res = Validator.check_dict(add_user)
        return res

        if existing_user:
            message = {"error": "username already exists!"}
            return message
        else:
            users.update(add_user)

        message = {
                    userid: add_user
                    }, 201
        return message

