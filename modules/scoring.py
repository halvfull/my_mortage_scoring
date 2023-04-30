# Import Libraries 
from app import app, db
from flask import request, render_template
from mymodels import Customer, Loan
from modules.register_customer import get_user_by_ssn

def calculate_score(loanAmount, equityAmount, salaryAmount):
    scorepoint = 0
    if loanAmount > 0:
        equity_ratio = equityAmount / loanAmount
        if equity_ratio >= 0.2:
            scorepoint += 50
        elif equity_ratio >= 0.1:
            scorepoint += 25
    if salaryAmount > 0:
        loan_ratio = loanAmount / salaryAmount
        if loan_ratio <= 5:
            scorepoint += 50
        elif loan_ratio <= 10:
            scorepoint += 25
    return scorepoint

@app.route('/scoring', methods=['GET', 'POST'])
def scoring():
    if request.method == 'POST':
        customerSSN = request.form['customerSSN']
        cust = get_user_by_ssn(customerSSN)
        if cust is None:
            return f"User with ssn: {customerSSN} does not exist"
        else:
            scorepoints = calculate_score(cust.loanAmount, cust.equityAmount, cust.salaryAmount)
            if scorepoints >= 0:
                loan = Loan(customerSSN=customerSSN, loanAmount=cust.loanAmount, scorepoints=scorepoints)
                db.session.add(loan)
                db.session.commit()
                return f"Loan granted to {cust.fullName} with ssn: {customerSSN}. Loan details: loanAmount={cust.loanAmount}."
            else:
                return f"Loan application rejected for {cust.fullName} with ssn: {customerSSN}. Score points: {scorepoint}."
    else:
        return render_template('scoring.html')

