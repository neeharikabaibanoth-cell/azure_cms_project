"""
The flask application package.
"""

import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# ✅ SETUP LOGGING HERE
app.logger.setLevel(logging.INFO)  # Log INFO and higher (e.g., WARNING, ERROR)
stream_handler = logging.StreamHandler()  # Log to console
stream_handler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
stream_handler.setFormatter(formatter)
app.logger.addHandler(stream_handler)

# ✅ Other setup
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# ✅ Import routes/views
import FlaskWebProject.views

