import string
from flask import Flask, jsonify
from validate_email import validate_email


class Validator:  # pragma: no cover

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

    def check_value(item1, item2, item3):
        if isinstance(item1, str):
            return jsonify({"error": "ID must be of type integer"}), 400
        if isinstance(item2, int) or isinstance(item3, int):
            return jsonify({"error": "content should be a string"}), 400
        if (type(item2) != str or (type(item2) != str)):
            return jsonify({"error": "invalid value!"}), 400
        if not item2 or not item3:
            return jsonify({"error": "invalid value!"}), 400
        if (item2 == " ") or (item3 == " "):
            return jsonify({"error": "invalid space!"}), 400
        if not item1:
            return jsonify({"error": "invalid value!"}), 400

    def validate_login(item1, item2, item3):
        if isinstance(item1, int) or isinstance(item1, int):
            return jsonify({"error": "invalid name"}), 400
        if (type(item1) != str or (type(item2) != str)):
            return jsonify({"error": "invalid name!"}), 400
        if not item1 or not item2:
            return jsonify({"error": "invalid name!"}), 400
        if (item1 == " ") or (item2 == " ") or (item3 == " "):
            return jsonify({"error": "invalid space!"}), 400
        # if isinstance(item3, int) < 10000000:
        #     return jsonify({"error": "Minimum length 8 characters"}), 400
        if len(item3) < 8:
            return jsonify({"error": "Invalid password!!"}), 400
        if not (item3):
            return jsonify({"error": "password field empty!!"}), 400
