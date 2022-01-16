from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__) 
app.config['SECRET_KEY']='thisismysecretkey12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCEHMY_TRACK_MODIFICATION']=False

db = SQLAlchemy(app)

app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465      
app.config['MAIL_USERNAME'] ='jalismahamud2055@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True 
mail = Mail(app) 

from main_app import views





