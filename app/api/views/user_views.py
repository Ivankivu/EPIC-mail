from datetime import datetime
import string
import logging
from flask import Flask, jsonify, Request, request, json, Response
from app import app
from app.api.database.dbconfig import DBconnect
from validate_email import validate_email
from app.utils import Validator
from app.api.models.users import User
from flask_jwt_extended import (
    JWTManager, create_access_token,
    get_jwt_identity, jwt_required, get_raw_jwt
)


jwt = JWTManager(app)


class ViewUser(object):

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({"message": "welcome to Epic mail"})

    @app.route('/api/v2/users', methods=['GET'])
    def get_all_contacts():
        if not users:
            return jsonify({"error": "no contacts found!!"})
        return jsonify(users)

    @app.route('/api/v2/auth/signup', methods=['POST'])
    def signup():

        response = User.signup_user()
        return response

    @app.route('/api/v2/auth/login', methods=['POST'])
    def login():

        response = User.get_user()
        return response

    @app.route('/api/v2/auth/logout', methods=['DELETE'])
    @jwt_required
    def logout():
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
        return jsonify({"msg": "Successfully logged out"}), 200
