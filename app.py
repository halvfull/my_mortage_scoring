from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import errorcode
from flaskext.mysql import MySQL

import pyodbc


app = Flask(__name__)


cnxn = pyodbc.connect(
    server="mortagescoringsqlserver.database.windows.net",
    database="MortageScoringDB",
    user='sqladmin',
    tds_version='7.4',
    password="Fridayfun123",
    port=1433,
    driver='FreeTDS'
)


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
