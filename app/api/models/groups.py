import string
from flask import Flask, request, Response, jsonify
from app import app
from app.utils import Validator


class Group:

    def __init__(self, group_id=int, group_name=str, user_role=bool):
        self.group_id = group_id
        self.group_name = group_name
        self.user_role = user_role
