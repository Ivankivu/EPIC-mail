import string
from datetime import datetime
from flask import Flask, request, Response, jsonify
from app.utils import Validator
from app import app

users = []
userid = Validator.auto_id(users)
messages = []
data = []
id = Validator.auto_id(messages)
parentMessageId = Validator.auto_id(messages)
createdOn = datetime


class User:

    def __init__(self, userid, firstname, lastname, email, password,):
        super(User, self).__init__()
        self.userid = userid
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def is_users(self):
        self.users = users


class Message:

    def __init__(self, id, parentMessageId, message, status,
                 receiverId, subject, data, senderId, createdOn):
        self.id = id
        self.parentMessageId = parentMessageId
        self.message = message
        self.status = status
        self.receiverId = receiverId
        self.senderId = senderId
        self.subject = subject
        self.createdOn = createdOn
        self.data = data

    def get_unread(self):
        unread_messages = [
            message for message in messages if
            message["receiverId"] == receiverId]
        if len(messages) == 0:
            return jsonify({'message': 'messages not found'})
            return response
        else:
            return unread_message
