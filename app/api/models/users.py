import string
import logging
from flask import Flask, request, Response, jsonify, json
from validate_email import validate_email
from app.api.database.dbconfig import DBconnect
from app import app
from app.utils import Validator
from flask_jwt_extended import (
    JWTManager, create_access_token,
    get_jwt_identity, jwt_required,
    get_raw_jwt
)


class User:

    def __init__(self, first_name, last_name, user_email, user_password, user_role):
        super(User, self).__init__()
        self.userid = userid
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.user_password = user_password
        self.user_role = user_role

    def get_user():
        info = request.get_json()
        user_email = info.get('user_email', None)
        user_password = info.get('user_password', None)
        is_valid = validate_email(user_email)
        if not is_valid:
            return jsonify(
                {"error": "invalid user_email!!",
                 "status": 400}), 400
        if not user_email and not user_password:
            return jsonify({"errror": "enter your credentials",
                            "status": 401}), 401
        if len(user_password) < 8:
            return jsonify({"error": "invalid user_password length!!",
                            "status": 400}), 400
        if not user_password:
            return jsonify({"error": "user_password field empty!!",
                            "status": 400}), 400
        else:
            try:
                with DBconnect() as cursor:
                    fetch_user_query = f""" SELECT user_id, user_email, user_password, user_role FROM users
                        WHERE user_email='{user_email}'
                    """
                    cursor.execute(fetch_user_query)
                    fetched_user = cursor.fetchone()
                    if fetched_user:
                        response = fetched_user
                    else:
                        return jsonify({"error": "user does not exist",
                                        "status": 404}), 404
                    my_identity = dict(
                        user_id=fetched_user.get('user_id'),
                        user_role=fetched_user.get('user_role')
                    )
                    user_identity = create_access_token(identity=my_identity)
                    return jsonify({"data": [{"token": user_identity}],
                                    "status": 200}), 200
            except Exception as e:
                logging.error(e)
                return jsonify({"error": str(e),
                                "status": 500}), 500

    def signup_user():
        """
        user to the app through the Signup
        """
        if request.method == 'POST':
            data = request.get_json()
            first_name = data["first_name"]
            last_name = data["last_name"]
            user_email = data["user_email"]
            user_password = data["user_password"]
            sql = '''INSERT INTO  users(first_name, last_name, user_email, user_password)
                     VALUES(%s, %s, %s, %s)'''
            try:
                with DBconnect() as cursor:
                    cursor.execute(
                        open("app/api/database/tables.sql", "r").read())
                    cursor.execute(
                        "SELECT user_id FROM users WHERE user_email = '%s'" % user_email)
                    response = cursor.fetchone()
                    if response:
                        return jsonify(
                            {"status": 409,
                             "error": "user_email already Taken!!."}), 409
                    else:
                        cursor.execute(
                            sql, (first_name, last_name, user_email, user_password,))
                        return jsonify(
                            {"message": "Successfully registered",
                             "status": 201}), 201
            except Exception as e:
                logging.error(e)
                return jsonify({"error": str(e),
                                "status": 500}), 500
