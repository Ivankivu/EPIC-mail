import string
import re
from flask import Flask, jsonify


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

    def validate_name(firstname, lastname):
        if firstname == "" or lastname == "":
            return jsonify({"error": "ffirstname is empty!!"})

        if firstname == " " and lastname == " ":
            return jsonify({"error": "Name cannot be spaces"})

        if not isinstance(firstname, str) or not isinstance(lastname, str):
            return jsonify({"error": "Name must be a string"})

        if firstname.startswith(string.digits):
            return jsonify({"error": "Name cannot start with a number"})
        return firstname or lastname

    def check_validation(email):
        for i in user:
            input = request.get_json
            message = i.strip() + ' is required'
            if not input[i]:
                return {'field': i, 'message': message}
            elif i.strip() == 'email' and not bool(match(r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", input[x])):
                response = ('email is invalid')
                return ({'field': i, 'message': response})
            elif i.strip() == 'password' and len(input[i].strip()) < 5:
                message = 'password should be atleast five characters'
                return message
