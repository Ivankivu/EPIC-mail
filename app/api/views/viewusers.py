from flask import Flask, jsonify, request, Response, json
from app import app
from app.api.models.users import User
from app.utils import Validator


class ViewUser:

    @app.route("/api/v1/users", methods=["GET"])
    def get_all_users():
        response = User.get_users()
        return jsonify(response)

    @app.route("/api/v1/auth/signup", methods=["POST"])
    def signup():

        response = User.signup_user()
        return jsonify(response), 201

    @app.route("/api/v1/auth/login", methods=["POST"])
    def login():

        response = User.login_user()
        return response
