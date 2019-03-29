from datetime import datetime
import string
import logging
from flask import Flask, jsonify, Request, request, json, Response
from app import app
from app.api.database.dbconfig import DBconnect
from validate_email import validate_email
from app.utils import Validator
from app.api.models.users import User
from app.api.models.messages import Message
from flask_jwt_extended import (
    JWTManager, create_access_token,
    get_jwt_identity, jwt_required,
    get_raw_jwt
)


class ViewMessage(object):

    @app.route('/api/v2/messages', methods=['POST', 'GET'])
    def compose_message():
        info = request.get_json()
        parentmessage_id = info.get("parentmessageId")
        receiverId = info.get("receiverId")
        subject = info.get("subject")
        message = info.get("message")
        status = "unread"
        sql = '''INSERT INTO messages(subject, message, receiverId, status) VALUES(%s, %s, %s, %s)'''
        try:
            with DBconnect() as cursor:
                cursor.execute(
                    open("app/api/database/tables.sql", "r").read())
                response = cursor.execute(
                    sql, (subject, message, receiverId, status,))
                query = "SELECT row_to_json(messages) FROM messages WHERE receiverId='%s'" % (
                    receiverId)
                cursor.execute(query, (receiverId))
                result = cursor.fetchone()
                if not result:
                    return jsonify({"error": "message failed!",
                                    "status": 400})
                return jsonify({"data": result,
                                "status": 201})

        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500

    @app.route('/api/v2/messages/unread', methods=['GET'])
    def unread_message():
        try:
            with DBconnect() as cursor:
                cursor.execute(
                    open("app/api/database/tables.sql", "r").read())
                query = "SELECT row_to_json(messages) FROM messages WHERE status='unread'"
                cursor.execute(query)
                result = cursor.fetchall()
                if not result:
                    return jsonify({"error": "no unread messages",
                                    "status": 400})
                return jsonify({"data": result,
                                "status": 201})

        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500

    @app.route('/api/v2/messages/<int:message_id>', methods=['GET', 'DELETE'])
    def get_single_message_delete(message_id):
        try:
            with DBconnect() as cursor:
                if request.method == "DELETE":
                    message_to_delete = "SELECT row_to_json(messages) FROM messages WHERE message_id ='{}'".format(message_id)
                                        
                    delete_existing_message = "DELETE FROM message WHERE message_id='{}'".format(message_id)
                   
                    # get  an item the delete the fetched item
                    cursor.execute(message_to_delete)
                    message_to_delete = cursor.fetchone()

                    if message_to_delete is not None:
                        try:
                            cursor.execute(delete_existing_message)
                            response = jsonify({'message': 'Message successfully deleted'}), 202
                        except Exception as error:
                            response = {'message': error}
                    else:
                        return jsonify(
                            {'errore': 'Message does not exist',
                            'status': 404}), 404

                    # return jsonify({"data": result,
                    #                 "status": 200}), 200
            # if request.method == "DELETE":
            #     sql = "DELETE FROM messages WHERE message_id=1"
            #     response = cursor.execute(sql)
            #     if not response:
            #         return jsonify({"error": "no messages found",
            #                         "status": 400})
            #     return jsonify({"error": "message deleted",
            #                     "status": 200})
        except Exception as e:
                logging.error(e)
                return jsonify({'message': str(e)}), 500
       
    @app.route('/api/v2/messages/sent', methods=['GET'])
    def sent_message():
        try:
            with DBconnect() as cursor:
                cursor.execute(
                    open("app/api/database/tables.sql", "r").read())
                query = "SELECT row_to_json(messages) FROM messages WHERE status='sent'"
                cursor.execute(query)
                result = cursor.fetchall()
                if not result:
                    return jsonify({"error": "no unread messages",
                                    "status": 400})
                return jsonify({"data": result,
                                "status": 201})

        except Exception as e:
            logging.error(e)
            return jsonify({'message': str(e)}), 500
