from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo,ValidationError
from ..models import User

class SignUpForm(FlaskForm):
    email = StringField('Enter a valid email address', validators=[Required(),Email()])
    username = StringField('Enter your preferred username',validators=[Required()])
    password = PasswordField('Enter an 8 character password',validators=[Required(),EqualTo('password_confirm',message='Passwords must match')])
    password_confirm = PasswordField('Confirm  Password', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is already taken')
    
    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Keep me signed in')
    submit = SubmitField('Sign In')