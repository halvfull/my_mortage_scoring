# Import Libraries 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Define app.
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)


import modules