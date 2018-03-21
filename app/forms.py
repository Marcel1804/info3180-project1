from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
    
class AddProfileForm(FlaskForm):
    firstname=StringField('Firstname', validators=[DataRequired()])
    lastname=StringField('Lastname', validators=[DataRequired()])
    gender=SelectField('Gender', choices=[('S','Select Gender'), ('M','Male'), ('F', 'Female')])
    email=StringField('Email', validators=[DataRequired()])
    location=StringField('Location', validators=[DataRequired()])
    bio=TextAreaField('Biography', validators=[DataRequired()])
    photo = FileField('Profile Picture',validators=[FileRequired(),FileAllowed(['jpg','png','Images only!'])])
    
class UserForm(FlaskForm):
      username=StringField('Username')
    
