from . import db
from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    gender=db.Column(db.String(80))
    location=db.Column(db.String(80))
    email=db.Column(db.String(80))
    bio=db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, first_name, last_name, username, gender, location, email, bio, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.gender=gender
        self.location=location
        self.email=email
        self.bio=bio
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' %  self.username
