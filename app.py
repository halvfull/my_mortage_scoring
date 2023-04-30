# Import Libraries 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Define app and configure database connection
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///MortageScoringDB"
db = SQLAlchemy(app)

# Import modules and models
import modules
from mymodels import Customer

# Create database tables if they don't exist yet
with app.app_context():
    db.create_all()

