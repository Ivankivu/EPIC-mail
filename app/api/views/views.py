from datetime import datetime
import string
import re
from flask import Flask, jsonify, Request, request, json, Response
from flask.views import MethodView
from app import app
from app.utils import Validator
from app.api.models.models import User, users, userid, Message, messages

# id = Validator.auto_id(dict, messages)
# parentMessageId = Validator.auto_id(dict, messages)
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
            "email": email,
            "password": password
        }
        if len(password) < 8:
            return jsonify({"error": "invalid email!!"}), 400
        if len(password) == 0:
            return jsonify({"error": "password field empty!!"}), 400
        if firstname == "" or lastname == "":
            return jsonify({"error": "firstname is empty!!"})
        if firstname == " " and lastname == " ":
            return jsonify({"error": "Name cannot be spaces"})
        if not isinstance(firstname, str) or not isinstance(lastname, str):
            return jsonify({"error": "Name must be a string"})
        if firstname.startswith(string.digits):
            return jsonify({"error": "Name cannot start with a number"})
        users.append(user_data)
        return jsonify({"message": "Account was created successfully!"}), 201

    @app.route('/api/v1/auth/login', methods=['POST'])
    def login():
        info = request.get_json()
        email = info.get('email', None)
        password = info.get('password', None)
        if re.compile('[!@#$%^&*:;?><.0-9]').match(email):
            return {"message": "Invalid characters not allowed"}
        if len(users) == 0:
            return jsonify({'message': 'No users found'})
        if not email and not password:
            return jsonify({"message": "enter your credentials"}), 401
        if len(password) < 8:
            return jsonify({"error": "invalid password length!!"}), 400
        if len(password) == 0:
            return jsonify({"error": "password field empty!!"}), 400
        else:
            uid = userid
            return jsonify({'message': "logged in"}), 200


class ViewMessage(MethodView):

    @app.route('/api/v1/messages', methods=['GET'])
    def all_messages():
        if len(messages) == 0:
            return jsonify({"message": "Inbox is empty!!"})
        else:
            return json.dumps(messages)

    @app.route('/api/v1/messages', methods=['POST'])
    def compose_message():

        info = request.get_json()
        id = info.get("id")
        parentMessageId = info.get("parentMessageId")
        receiverId = info.get("receiverId")
        senderId = userid
        subject = info.get("subject")
        message = info.get("message")
        status = "sent"
        createdOn = info.get("createdOn")
        message_data = {
            "status": 201,
            "data": {
                "id": len(messages)+1,
                "createdOn": str(datetime.now()),
                "message": message,
                "status": status,
                "subject": subject,
                "senderId": senderId,
                "receiverId": receiverId
            }
        }
        if senderId == "":
            return jsonify({"error": "senderID can't be an empty field!!"})
        else:
            messages.append(message_data)
        return jsonify(message_data)

    @app.route('/api/v1/messages/unread', methods=['GET'])
    def unread_message():
        if len(messages) == 0:
            return jsonify({"error": "no new mail."})
        if ['status'] != 'unread':
            return jsonify({"error": "no mail by  user found!"})
        return jsonify(messages)

    @app.route('/api/v1/messages/<int:id>', methods=['GET'])
    def single_message(id):
        if len(messages) == 0:
            return jsonify({"message": "Inbox is empty!!"})
        for message in messages:
            if message["data"]["id"] == '':
                response = {"error": "empty field"}
                return response
            if isinstance((message["data"]["id"] == 0), str):
                response = {'message': 'ID must be of type integer'}
                return response
            if message["data"]["id"] == id:
                return jsonify(message)
