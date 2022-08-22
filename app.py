from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

d = SQLAlchemy(application)

from routes import *

if __name__ == '__main__':
    application.run(debug=True,host='0.0.0.0',port='8085')