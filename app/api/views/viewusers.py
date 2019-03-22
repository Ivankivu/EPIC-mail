from flask import Flask, jsonify, Request, request, json, Response
from flask.views import MethodView
from app import app
from app.api.models.users import User, users, userid


class ViewUser(MethodView):

    @app.route("/api/v1/users", methods=["GET"])
    def all():
        return jsonify(users)

    @app.route("/api/v1/auth/signup", methods=["POST"])
    def signup():
        data = request.get_json()
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        password = data["password"]
        user_data = {
            "userid": userid,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password": password
        }
        users.append(user_data)
        return jsonify({"message": "Account was created successfully!"}), 201

    @app.route('/api/v1/auth/login', methods=['POST'])
    def login():
        info = request.get_json()
        email = info.get('email', None)
        password = info.get('password', None)
        if len(users) == 0:
            return jsonify({'message': 'No users found'})
        for user in users:
            if user["email"] != email and user["password"] != password:
                return jsonify({'message': "login failed!!"}), 400
            else:
                return jsonify({'message': "logged in"}), 200
