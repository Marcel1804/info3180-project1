from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "372ijma/.D/V,A,KK,ASK,1mejlADK\S][SP;SLKK2I231JHRMWGU2009SL<AFUJMASJS"  # you should make this more random and unique
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lab5:akeam1804@localhost/lab5"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # necessary to tell Flask-Login what the default route is for the login page
login_manager.login_message_category = "info"  # customize the flash message category

app.config.from_object(__name__)
from app import views
