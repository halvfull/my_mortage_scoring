from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import errorcode
from flaskext.mysql import MySQL
from sqlalchemy import insert, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy



# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine, MetaData



# DEFINE THE DATABASE CREDENTIALS
user = 'sqladmin'
password = 'Fridayfun123'
host = 'mortagescoringsqlserver.database.windows.net'
port = 1433
database = 'MortageScoringDB'

def get_connection():
	return create_engine(
		url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
			user, password, host, port, database
		)
          
	)


"""
# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT

engine = create_engine(
		url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
			user, password, host, port, database), echo = True)
base = declarative_base()
class person(base):
    __tablename__='people'
    name = Column(String, primary_key=True)
    age = Column(Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

Session = sessionmaker(bind=engine)
session = Session()
a_person = person('personnavnet', 22)
session.add(a_person)
session.commit()
"""
"""base = declarative_base()



base.metadata.create_all(engine)
"""
app = Flask(__name__)
db=SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"]=host

try:
		# GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
	engine = get_connection()
	print(f"Connection to the {host} for user {user} created successfully.")
    
except Exception as ex:
	print("Connection could not be made due to the following error: \n", ex)
        
with app.app_context():
    db.create_all()

class person(db.Model):
    __tablename__='people'
    name = db.Column(String, primary_key=True)
    age = db.Column(Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age



"""
try:
    cnx = mysql.connector.connect(user='sqladmin', password='Fridayfun123',
                                host='mortagescoringsqlserver.database.windows.net',
                                database='MortageScoringDB',
                                port=1403)
    cnx.close()
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
"""


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello mfucker - how are you doing?')


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message='sorry' + name + ', not old enough '), 401
    else:
        return jsonify(message='welcome ' + name + ', you are old enough!')


@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message='sorry' + name + ', not old enough '), 401
    else:
        return jsonify(message='welcome ' + name + ', you are old enough!')

""" 
# database models
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Planet(db.Model):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)

"""
if __name__ == '__main__':
    app.run()
