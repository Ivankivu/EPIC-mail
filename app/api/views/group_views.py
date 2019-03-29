
import string
import logging
from flask import Flask, jsonify, Request, request, json, Response
from app import app
from app.api.database.dbconfig import DBconnect
from validate_email import validate_email
from app.utils import Validator
from app.api.models.users import User
# from app.api.models.groups import fr
from flask_jwt_extended import (
    JWTManager, create_access_token,
    get_jwt_identity, jwt_required,
    get_raw_jwt
)


class Viewgroup(object):

    @app.route('/api/v2/groups', methods=['POST', 'GET'])
    def create_group():
        info = request.get_json()
        group_name = info.get("group_name")
        sql = '''INSERT INTO groups(group_name) VALUES(%s)'''
        try:
            with DBconnect() as cursor:
                cursor.execute(
                    open("app/api/database/tables.sql", "r").read())
                if request.method == "POST":
                    response = cursor.execute(sql, (group_name,))
                    query = "SELECT * FROM groups WHERE group_name='%s'" % (
                        group_name)
                    cursor.execute(query, (group_name))
                    result = cursor.fetchone()
                    if not result:
                        return jsonify({"error": "group failed!",
                                        "status": 400})
                    return jsonify({"data": result,
                                    "status": 201})
                if request.method == "GET":
                    query = "SELECT * FROM groups"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
        except Exception as e:
            logging.error(e)
            return jsonify({'group': str(e)}), 500

    @app.route('/api/v2/groups/<group_id>', methods=['DELETE'])
    def get_single_group_delete(group_id):
        try:
            with DBconnect() as cursor:
                if not type(group_id, int):
                    return jsonify({"error": "invalid value",
                                    "status": 400}), 400
                if request.method == "DELETE":
                    sql = "DELETE FROM groups WHERE group_id = '{}'".format(group_id)
                    cursor.execute(sql)
                    return jsonify({"error": "group deleted",
                                    "status": 200}), 200
                return jsonify({"error": "group not found",
                                "status": 400}), 400
               
        except Exception as e:
                logging.error(e)
                return jsonify({'group': str(e)}), 500
       
    @app.route('/api/v2/groups/<int:group_id>/users', methods=['POST'])
    def add_user_to_group(group_id):
        info = request.get_json()
        users = info.get("users")
        try:
            with DBconnect() as cursor:
                sql = "insert into groups(users) values(array[%s]) WHERE group_id ='%s'"% (group_id, users)
                cursor.execute(sql, (group_id, users,))
                result = cursor.fetchone()
                if not result:
                    return jsonify({"error": "user not added",
                                    "status": 400})
                return jsonify({"data": result,
                                "status": 201})

        except Exception as e:
            logging.error(e)
            return jsonify({'group': str(e)}), 500
