from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_user(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("Pleae use a different email address.")


class EditProfileForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    about_me = TextAreaField('About Me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Change Profile')

    def __init__(self, orignial_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.orignial_username = orignial_username

    def validate_username(self, username):
        if username.data != self.orignial_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user:
                raise ValidationError('Please use a different username.')
