import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_uploads import configure_uploads, IMAGES, UploadSet

# Create a login manager object
login_manager = LoginManager()

app = Flask(__name__)

app.config.from_pyfile('config.py')
app.config["UPLOADED_IMAGES_DEST"] = "userImages"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Database configuration
db = SQLAlchemy(app)
Migrate(app, db)

# Pass app into the login manager and send users to login view
login_manager.init_app(app)
login_manager.login_view = "login"

images = UploadSet("images", IMAGES)
configure_uploads(app, images)