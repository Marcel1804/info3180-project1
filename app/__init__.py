from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "372ijma/.D/V,A,KK,ASK,1mejlADK\S][SP;SLKK2I231JHRMWGU2009SL<AFUJMASJS"  # you should make this more random and unique
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://akeam:akeam1804@localhost/project"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # added just to suppress a warning
app.config['UPLOAD_FOLDER']= "./app/static/uploads" # using a config value

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
