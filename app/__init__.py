from flask import Flask
from app.config import env_config 

app = Flask(__name__)

from app.api.views.views import *



