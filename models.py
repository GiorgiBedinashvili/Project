from ext import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Shawarma(db.Model):

    __tablename__="shawarma"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    image = db.Column(db.String())
    information = db.Column(db.String())

class Posts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String())
    photo = db.Column(db.String())
    username = db.Column(db.String())
    comments = db.relationship('Comments', backref='post', lazy=True)

class Comments(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    comment = db.Column(db.String())
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))



class User(db.Model, UserMixin):

    __tablename__="user"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    gender = db.Column(db.String())
    birth = db.Column(db.String())
    email = db.Column(db.String())
    role = db.Column(db.String())


    def __init__(self, username, password,birth, email, gender, role="Guest"):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role
        self.birth = birth
        self.email = email
        self.gender = gender



    def check_paasword(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)