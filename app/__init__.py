
from flask import Flask

app = Flask(__name__)

from app.api.views.view_parcels import ViewParcels
from app.api.views.viewsusers import ViewUser
