from flask import Flask, render_template
from forms import RegisterForm
from forms import PostForm
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "erfvhuq771b314c6HH"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"