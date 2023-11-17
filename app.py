import os
from flask import Flask
from flask_cors import CORS

from config import config_app

app = Flask(__name__)
CORS(app)
config_app(app, os.environ["PUBLIC_URL"])
