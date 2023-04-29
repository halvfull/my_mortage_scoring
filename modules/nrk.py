# Import Libraries 
from app import app, db
from flask import redirect

# Define route "/code".
class Customer(db.Model):
  ssn = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String, unique=True, nullable=False)

@app.route('/code')
def code():
  with app.app_context():

    db.create_all()
    exists = Customer.query.filter_by(ssn=12233).first()
    if not exists:
      db.session.add(Customer(ssn=12233, first_name="ingrid"))
      db.session.commit()
  
      #users = db.session.execute(db.select(Customer)).scalars()
    return redirect('https://nrk.no')
