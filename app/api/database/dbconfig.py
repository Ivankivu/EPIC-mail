import psycopg2
from psycopg2 import extras as IK
from app.config import env_config
from app import app as ap
from pprint import pprint
from urllib.parse import urlparse


class DBconnect(object):

    def __init__(self):
        self.credentials = dict(
            dbname='postgres',
            user='postgres',
            password='postgres',
            host='localhost',
            port=5432
        )

    def __enter__(self):

        if ap.config.get('ENV') == 'development':
            dbname = env_config['development'].DATABASE
            self.credentials['dbname'] = dbname

        if ap.config.get('ENV') == 'testing':
            dbname = env_config['testing'].DATABASE
            self.credentials['dbname'] = dbname

        # if ap.config.get('ENV') == 'production':
        #     dbname = env_config['production'].DATABASE
        #     self.credentials['host'] = env_config['production'].HOST
        #     self.credentials['user'] = env_config['production'].USER
        #     self.credentials['password'] = env_config['production'].PASSWORD
        #     self.credentials['dbname'] = dbname

        try:
            self.conn = psycopg2.connect(
                **self.credentials, cursor_factory=IK.RealDictCursor)
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            return self.cursor

        except Exception as error:
            print(f"error: {error}")

    def __exit__(self, exception_type, exception_val, exception_traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
