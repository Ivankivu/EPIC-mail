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

    def doesnot_exist(item):
        if not item or len(item) == 0:
            return jsonify({
                "error": 'Sorry! Item should at least have three characters'
            }), 400

    def is_not_integer(item):
        if type(item) == int:
            return jsonify({
                "error": 'Sorry item should be an integer'
            }), 400

    def is_negative(item):
        if item in item_list:
            if item['item_id'] != item['item_id']:
                item_list.append(item)

    def validate_password(item):
        if len(password) < 8:
            return jsonify({"error": "invalid email!!"}), 400

        if len(password) == 0:
            return jsonify({"error": "password field empty!!"}), 400

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

    def get_timestamp():
        return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

    def check_dict(dict):
        items = list()
        item = dict()
        for item in items:
            if item['item'] == '':
                return jsonify({"error": 'empty list'})
            if isspace(item):
                return jsonify({"error": 'empty list'})
            if not isalpha(item):
                return jsonify({"error": 'invalid credentials'})
