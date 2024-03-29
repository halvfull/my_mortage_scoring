
# My Mortgage Scoring App
This is a web application for a simplified loan scoring applications. It allows users to enter their personal and financial information and get an automated score that indicates whether they are likely to qualify for a loan. The application is built using Flask, SQLAlchemy, and SQLite and is hosted on Azure.

 
## Installation

To install and run the application, follow these steps:
(Python 3.9.16 used)

 1. Clone the repository
 2. Install the required dependencies by running pip install -r requirements.txt
 3. Start the application by running python run.py
 4. Navigate to http://localhost:5000/ in your browser to access the application
  
  

## Deployment
The application is deployed on Azure and is automatically updated whenever changes are made to the repository. You can access the deployed application at the following URL:

https://mymortagescoringapp.azurewebsites.net/

  
  

## Usage
To use the application, follow these steps:

Register a new customer as by entering your SSN, Full name, Loan amount, Equity amount and Salary amount.
(Note, please do not submit any sensitive data, as real SSN)
Click the "Submit" button and choose to accept or decline the loan. If your score is above a certain threshold, you will be offered a loan. It will grant the loan and store the loan in the database, if you click accept. If you click decline, only the score will be stored.
