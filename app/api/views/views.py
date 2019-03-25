from datetime import datetime
import string
import re
from flask import Flask, jsonify, Request, request, json, Response
from flask.views import MethodView
from validate_email import validate_email
from app import app
from app.utils import Validator
from app.api.models.models import User, users, userid, Message, messages

createdOn = datetime.now()


class ViewUser(MethodView):

    @app.route("/api/v1/users", methods=["GET"])
    def all():
        if len(users) == 0:
            return jsonify({"error": "no contacts found!!"})
        return jsonify(users)

    @app.route("/api/v1/auth/signup", methods=["POST"])
    def signup():
        data = request.get_json()
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        password = data["password"]
        user_data = {
            "userid": len(users)+1,
            "firstname": firstname,
            "lastname": lastname,
            "email": email
        }
        is_valid = validate_email(email)
        if not is_valid:
            return jsonify({"error": "invalid email!!"}), 400
        check_name = Validator.validate_string(firstname, lastname)
        if check_name:
            return check_name
        users.update(user_data)
        return jsonify({"message": "Account was created successfully!"}), 201

    @app.route('/api/v1/auth/login', methods=['POST'])
    def login():
        info = request.get_json()
        email = info.get('email', None)
        password = info.get('password', None)
        is_valid = validate_email(email)
        if not is_valid:
            return jsonify({"error": "invalid email!!"}), 400
        if len(users) == 0:
            return jsonify({'message': 'No users found'})
        if not email and not password:
            return jsonify({"message": "enter your credentials"}), 401
        if len(password) < 8:
            return jsonify({"error": "invalid password length!!"}), 400
        if len(password) == 0:
            return jsonify({"error": "password field empty!!"}), 400
        else:
            return jsonify({'message': "logged in"}), 200


class ViewMessage(MethodView):

    @app.route('/api/v1/messages', methods=['POST', 'GET'])
    def compose_message():
        if request.method == "POST":
            info = request.get_json()
            parentMessageId = info.get("parentMessageId")
            receiverId = info.get("receiverId")
            senderId = userid
            subject = info.get("subject")
            message = info.get("message")
            status = "sent"
            message_data = {
                "status": 201,
                "data": {
                    "id": len(messages)+1,
                    "createdOn": str(datetime.now()),
                    "message": message,
                    "status": status,
                    "subject": subject,
                    "senderId": senderId,
                    "receiverId": receiverId,
                    "parentMessageId": parentMessageId
                }
            }
            if not senderId:
                return jsonify(
                    {"error": "senderID can't be an empty field!!"}), 404
            else:
                messages.append(message_data)
            return jsonify(message_data), 200
        if request.method == "GET":
            if len(messages) == 0:
                return jsonify({"message": "Inbox is empty!!"})
            else:
                return json.dumps(messages)

    @app.route('/api/v1/messages/unread', methods=['GET'])
    def unread_message():
        if not messages:
            return jsonify({"error": "no new mail."}), 404
        if ['status'] != 'unread':
            return jsonify({"error": "no mail by  user found!"}), 404
        return jsonify(messages)

    @app.route('/api/v1/messages/<int:id>', methods=['GET', 'DELETE'])
    def get_single_message_delete(id):
            if len(messages) == 0:
                return jsonify({"message": "Inbox is empty!!"}), 404
            if not isinstance(id, int):
                    return jsonify({"error": "invalid"}), 400
            for message in messages:
                response = (message["data"]["id"] == id)
                if response:
                    if request.method == "GET":
                        return jsonify(message)
                    else:
                        messages.remove(message)
                        return jsonify({"message": "message deleted!!"})

    @app.route('/api/v1/messages/sent', methods=['GET'])
    def sent_message():
        if len(messages) == 0:
            return jsonify({"error": "no messages found!!"}), 404
        if ['status'] == 'sent' and ["userid"] == userid:
            return jsonify({"error": "no messages by  user found!!"}), 404
        return jsonify(messages)
