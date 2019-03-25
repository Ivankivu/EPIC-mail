import string
import re
from flask import Flask, jsonify
from app import app
from validate_email import validate_email


class Validator:

    def auto_id(list):
        global id
        if len(list) == 0:
            id = len(list)+1
        else:
            id = list[-1]+1
        return id

    def is_empty(list):
        if len(list) == 0:
            return jsonify({"error": 'empty list'})

    def validate_string(item1, item2):
        if item1 == "" or item2 == "":
            return jsonify({"error": "value is empty!!"})
        if item1 == " " and item2 == " ":
            return jsonify({"error": "Name cannot be spaces"})
        if not isinstance(item1, str) or not isinstance(item2, str):
            return jsonify({"error": "Name must be a string"})
        if item1.startswith(string.digits) or item2.startswith(string.digits):
            return jsonify({"error": "Name cannot start with a number"})

    def check_validation(email):
        is_valid = validate_email(email)
        if not is_valid:
            return jsonify({"error": "invalid email!!"}), 400

    def check_string(*args):
        if type(*args) != str:
            return jsonify({"error": "invalid value!"}), 400
