import string
import logging
from datetime import datetime
from flask import Flask, request, Response, jsonify
from validate_email import validate_email
from app.api.database.dbconfig import DBconnect
from app import app
from app.utils import Validator
from app.api.models.users import User


class Message:

    def __init__(self, parentMessageId, message, status,
                 receiverId, subject, senderId, message_id):
        self.parentMessageId = parentMessageId
        self.message = message
        self.status = status
        self.receiverId = receiverId
        self.senderId = senderId
        self.subject = subject
        self.message_id = message_id