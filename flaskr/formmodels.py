from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length,Email

class RegistrationForm(FlaskForm):
    empid = StringField(name='Employee ID', validators=[DataRequired(), Length(min=1, max=4)])
    first_name = StringField(name='First name', validators=[DataRequired(), Length(min=2, max=15)])
    last_name = StringField(name='Last name', validators=[DataRequired(), Length(min=2, max=15)])
    title = StringField(name='Title', validators=[DataRequired(), Length(min=4, max=15)]) 
    email = EmailField(name='Email', validators=[DataRequired(), Email()])
    password = PasswordField(name='Password', validators=[DataRequired(), Length(min=6)])
    submitbutton = SubmitField(name='Sign up')

class LoginForm(FlaskForm):
    email = EmailField(name='Email', validators=[DataRequired(), Email()])
    password = PasswordField(name='Password', validators=[DataRequired(), Length(min=6)])
    loginbutton = SubmitField(name='Login')

class SearchPage(FlaskForm):
    first_name = StringField(validators=[DataRequired(), Length(min=2, max=15)])
    submitbutton = SubmitField(name='Search')