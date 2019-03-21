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
            "id": userid,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "is_admin": is_admin
        }
        users.append(user_data)
        return jsonify({"message": "Account was created successfully!"}), 201
