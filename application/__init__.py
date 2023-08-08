from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField

import secrets

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = secrets.token_hex(8)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.static_url_path = '/static'
app.static_folder = 'static'
db = SQLAlchemy(app)

from application import routes
