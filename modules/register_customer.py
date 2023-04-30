# Import Libraries 
from app import app, db
from flask import request
from mymodels import Customer

#checks if user exists in DB
def get_user_by_ssn(customerSSN):
   customer = Customer.query.filter_by(customerSSN=customerSSN).first()
   return customer


@app.route('/register', methods= ['POST'])
def register_customer():
   customerSSN = request.args.get('customerSSN')
   fullName = request.args.get('fullName')
   loanAmount = request.args.get('loanAmount')
   equityAmount = request.args.get('equityAmount')
   salaryAmount = request.args.get('salaryAmount')

   cust= get_user_by_ssn(customerSSN)
   if cust is not None:
      return  f"User {cust.fullName}  with ssn: {cust.customerSSN} already exists"
   else:
      cust = Customer(customerSSN=customerSSN, fullName=fullName, loanAmount=loanAmount, equityAmount=equityAmount, salaryAmount=salaryAmount)
      db.session.add(cust)
      db.session.commit()
      return f"Sucessfully registered new user: {cust.fullName}  with ssn: {cust.customerSSN}"
