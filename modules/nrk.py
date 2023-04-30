# Import Libraries 
from app import app, db
from flask import redirect
from mymodels import Customer

@app.route('/code')
def code():

    exists = Customer.query.filter_by(customerSSN=12233).first()
    if not exists:
      db.session.add(Customer(customerSSN=12233, fullName="ingrid", loanAmount=200, equityAmount=2000,salaryAmount=4))
      db.session.commit()
  
      #users = db.session.execute(db.select(Customer)).scalars()
    return redirect('https://nrk.no')
