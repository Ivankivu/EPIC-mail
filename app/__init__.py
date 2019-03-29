from flask import Flask
from app.config import env_config

app = Flask(__name__)

from app.api.views.user_views import ViewUser
from app.api.views.message_views import ViewMessage
from app.api.views.group_views import Viewgroup
