#Collection of all dataclasses used
from app import db

class Customer(db.Model):
  customerSSN = db.Column(db.Integer, primary_key=True)
  fullName = db.Column(db.String, unique=True, nullable=False)
  loanAmount  = db.Column(db.Float, nullable=False)
  equityAmount = db.Column(db.Float, nullable=False)
  salaryAmount = db.Column(db.Float, nullable=False)


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customerSSN'))
    score = db.Column(db.Integer, nullable=False) 


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customerSSN'))
    score = db.Column(db.Integer, nullable=False)