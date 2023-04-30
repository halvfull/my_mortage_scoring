# Import Libraries 
from app import app, db
from flask import request, render_template
from mymodels import Customer, Loan, Score
from modules.register_customer import get_user_by_ssn

def calculate_score(loanAmount, equityAmount, salaryAmount):
    #Calculates score points for given customer parameters, returns total score points.
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
    #Handles loan scoring requests from users.
    scorepoint_threshold = 20
    if request.method == 'POST':
        customerSSN = request.args.get('customerSSN')
        cust = get_user_by_ssn(customerSSN)
        if cust is None:
            return f"User with ssn: {customerSSN} does not exist"
        else:
            # Check if the customer already has a loan.
            existing_loan = Loan.query.filter_by(customerSSN=customerSSN).first()
            if existing_loan is not None:
                return f"{cust.fullName} with ssn: {customerSSN} already has a loan."
            
            scorepoints = calculate_score(cust.loanAmount, cust.equityAmount, cust.salaryAmount)
            score = Score(customerSSN=customerSSN,loanAmount=cust.loanAmount,scorepoints=scorepoints)
            db.session.add(score)
            db.session.commit()
            if scorepoints >= scorepoint_threshold:
                if request.form['action'] == 'accept':
                    loan = Loan(customerSSN=customerSSN, loanAmount=cust.loanAmount, scorepoints=scorepoints, score_id=score.id)
                    db.session.add(loan)
                    db.session.commit()
                    return f"Loan granted to {cust.fullName} with ssn: {customerSSN}. Loan details: loanAmount={cust.loanAmount}. Score points: {scorepoints}  "
                elif ['action'] == 'decline':
                    return "Loan denied "
                else:
                    return f"You have chosen to reject the loan."
            else:
                return f"Loan denied. The Loan application rejected for {cust.fullName} with ssn: {customerSSN}. Your points: {scorepoints}, which is below threshold of {scorepoint_threshold} points minimum."
    else:
        return render_template('scoring.html')