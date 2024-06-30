from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, DateField, EmailField, SelectField,  SubmitField, TextAreaField

from wtforms.validators import DataRequired, Length, equal_to
from flask_wtf.file import FileField, FileRequired


class RegisterForm(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired()])
    email = EmailField("Enter your e-mail", validators=[DataRequired()])
    password = PasswordField("Enter your password", validators=[DataRequired(), Length(min=8, max=64)])
    repeat_password = PasswordField("Repeat your password", validators=[DataRequired(), Length(min=8, max=64), equal_to("password", message="passwords don't mach")])
    birth = DateField("Enter your date of birth", validators=[DataRequired()])
    gender = SelectField("Select your gender", choices=["Male", "Female", "Other"])
    submit = SubmitField("Submit")

class PostForm(FlaskForm):
    post = TextAreaField("Write your post", validators=[DataRequired()])
    photo = FileField("Add your photo")
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired()])
    password = PasswordField("Enter your password", validators=[DataRequired(), Length(min=8, max=64)])
    submit = SubmitField("Log in")



class CardForm(FlaskForm):
    name = StringField("Add the name", validators=[DataRequired()])
    image = FileField("Add the image")
    information = TextAreaField("Add info")
    submit = SubmitField("Submit")


class CommentForm(FlaskForm):
    comment = StringField("Write your comment here", validators=[DataRequired()])
    submit = SubmitField("Add")