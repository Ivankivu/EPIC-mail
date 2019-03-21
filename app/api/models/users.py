import string
from flask import Flask, request, Response, jsonify
from app.utils import Validator
from app import app

users = []
userid = Validator.auto_id(dict, users)


class User:

    def __init__(self, *args):
        super(User, self).__init__()
        self.userid = userid
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.is_admin = False
