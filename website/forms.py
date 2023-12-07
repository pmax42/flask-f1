from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from flask_login import current_user
from .models import User

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[Length(min=10, max=10), Optional()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Custom validation for email
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists. Please use a different email.')
        
    def validate_phone_number(self, phone_number):
        # If phonne number is not empty, check only numbers are entered
        if phone_number.data:
            if not phone_number.data.isdigit():
                raise ValidationError('Must contain only numbers.')
        
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "name@gmail.com"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "••••••"})
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[Length(min=10, max=10), Optional()])
    submit = SubmitField('Update')

    # Custom validation for email
    def validate_email(self, email):
        # If email is changed, check if it already exists
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already exists. Please use a different email.')

    def validate_phone_number(self, phone_number):
        # If phonne number is not empty, check only numbers are entered
        if phone_number.data:
            if not phone_number.data.isdigit():
                raise ValidationError('Must contain only numbers.')
