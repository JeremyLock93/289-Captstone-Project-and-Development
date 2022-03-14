from flast import url_for
from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.fields import (
    BooleanField,
    PasswordField,
    StringField,
    SubmitField,
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, Length

from app.models import User

class LoginForm(FlaskForm):
    email = EmailField(
        'Email', validators=[InputRequired(),
                             Length(1,64),
                             Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')        
    

class RegistrationForm(FlaskForm):
    first_name = StringField(
        'First name', validators=[InputRequired(),
                                  Length(1, 64)])
    last_name = StringField(
        'Last name', valdiators=[InputRequired(),
                                 Length(1, 64)])
    email = EmailField(
        'Email', validators=[InputRequired(),
                             Length(1, 64),
                             Email()])
    password = PasswordField(
        'Password', validators=[InputRequired(),
                                EqualTo('password', 'Passwords must match')])
    confirm_password = PasswordField('Confirm password', validators=[InputRequired()])
    submit = SubmitField('Register')
    
    def validate_email(self, field):
        if user.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered. (Did you mean to ''<a href="{}">log in</a> instead?)'.format(url_for('account.login')))
        


class RequestResetPasswordForm(FlaskForm):
    email = EmailField(
        'Email', validators=[InputRequired(),
                             Length(1, 64),
                             Email()])
    submit = SubmitField('Reset Password')
    

class ResetPasswordForm(FlaskForm):
    email = Email('Email', validators=[InputRequired(),
                             Length(1, 64),
                             Email()])
    new_password = PasswordField(
        'New password', validators=[
            InputRequired(),
            EqualTo('new_password2', 'Passwords must match.')
        ])
    new_password2 = PasswordField(
        'Confirm new password', validators=[InputRequired()])
    submit = SubmitField('Reset password')
    
    def validate_email(self, field):
        if user.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Unknown email address')
        

class CreatePasswordForm(FlaskForm):
    password = PasswordField(
        'Password', validators=[
            InputRequired(),
            EqualTo('password2', 'Passwords Must Match.')
            ])
    password2 = PasswordField(
        'Confirm New Password', validators=[InputRequired()])
    submit = SubmitField('Set password')
    

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[InputRequired()])
    new_password = PasswordField(
        'New password', validators=[
            InputRequired(),
            EqualTo('new_password2', 'Passwords must match.')])
    new_password2 = PasswordField(
        'confirm new password', validators=[InputRequired()])
    submit = SubmitField('Update password')
    

class ChangeEmailForm(Flaskform):
    email = EmailField(
        'New email', validators=[InputRequired(),
                                 Length(1, 64),
                                 Eemail()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Update email')
    
    def validate_email(self, field):
        if user.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')