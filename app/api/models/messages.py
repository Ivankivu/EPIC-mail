import string
from datetime import date
from flask import Flask, request, Response, jsonify
from app.utils import Validator
from app import app

messages = []
data = []
message_id = Validator.auto_id(dict, messages)
parentMessageId = Validator.auto_id(dict, messages)
createdOn = date


class Message:

    def __init__(self, **kwargs):
        self.message_id = kwargs.get("message_id")
        self.parentMessageId = kwargs.get("parentMessageId")
        self.message = kwargs.get("message")
        self.status = kwargs.get("status")
        self.receiverId = kwargs.get("receiverId")
        self.senderId = kwargs.get("senderId")
        self.subject = kwargs.get("subject")
        self.createdOn = kwargs.get("createdOn")

    def new_message(self, **items):
        items = request.get_json()

        message = items.get("message")
        status = items.get("status")

        sent = {
            "status": status,
            "data": [{
                "message_id": message_id,
                "createdOn": createdOn,
                "message": message,
                "parentMessageId": parentMessageId
            }]
            }

        messages.append(sent)
        result = {"message": "Message Sent!"}
        return result

    def all_messages():
        if len(messages) == 0:
            return ("Inbox is empty!!")
        else:
            print("yahe")
