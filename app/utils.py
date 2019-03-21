import string
from flask import Flask


class Validator:

    def auto_id(item_id, list):
        global id
        if len(list) != 0:
            last_item = (list)[-1]
            id = last_item.get(item_id) + 1
        else:
            id = 1
        return id

    def is_empty(list):
        if len(list) == 0:
            return jsonify({'message': 'empty list'})

    def doesnot_exist(item):
        if not item or len(item) == 0:
            return jsonify({
                'message': 'Sorry! Item should at least have three characters'
            }), 400

    def is_not_integer(item):
        if type(item) == int:
            return jsonify({
                'message': 'Sorry item should be an integer'
            }), 400

    def is_negative(item):
        if item in item_list:
            if item['item_id'] != item['item_id']:
                item_list.append(item)

    def get_timestamp():
        return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

    def check_dict(dict):
        items = list()
        item = dict()
        for item in items:
            if item['item'] == '':
                return jsonify({'message': 'empty list'})
            if isspace(item):
                return jsonify({'message': 'empty list'})
            if not isalpha(item):
                return jsonify({'message': 'invalid credentials'})
