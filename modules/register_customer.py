# Import Libraries 
from app import app, db
from flask import request, render_template, redirect, url_for
from mymodels import Customer

#checks if user exists in DB
def get_user_by_ssn(customerSSN):
   customer = Customer.query.filter_by(customerSSN=customerSSN).first()
   return customer

''' 
#old routing without front-end
@app.route('/register', methods= ['GET', 'POST'])
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
'''

@app.route('/register-form')
def register_form():
    return render_template('register.html')


@app.route('/register', methods=['GET', 'POST'])
def registerer_cust():
    if request.method == 'POST':
        customerSSN = request.form['customerSSN']
        fullName = request.form['fullName']
        loanAmount = request.form['loanAmount']
        equityAmount = request.form['equityAmount']
        salaryAmount = request.form['salaryAmount']

        cust = get_user_by_ssn(customerSSN)
        if cust is not None:
            return f"User {cust.fullName} with ssn: {cust.customerSSN} already exists"
        else:
            cust = Customer(customerSSN=customerSSN, fullName=fullName, loanAmount=loanAmount, equityAmount=equityAmount, salaryAmount=salaryAmount)
            db.session.add(cust)
            db.session.commit()
            return redirect(url_for('scoring', customerSSN=customerSSN))
    else:
        return render_template('register.html')