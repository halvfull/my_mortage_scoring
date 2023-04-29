# Import Libraries 
from app import app, db
from flask import redirect
from modules.nrk import Customer


@app.route('/jak')
def vg():
  with app.app_context():
    db.create_all()
    exists = Customer.query.filter_by(ssn=987).first()
    if not exists:
        db.session.add(Customer(ssn=987, first_name="jakob"))
        db.session.commit()

      #users = db.session.execute(db.select(Customer)).scalars()
    return redirect('https://vg.no')
