from flask import render_template, redirect
from forms import RegisterForm, PostForm, LoginForm, CardForm, CommentForm
from ext import app
from ext import db
from models import Shawarma,Posts, Comments
from models import User
from flask_login import login_user, logout_user, current_user, login_required
from init_db import admin_user


@app.route("/")
def index():
    shawarmas = Shawarma.query.all()
    return render_template("bootstrap.html", shawarmas=shawarmas)


@app.route("/AdminOnly", methods=["GET", "POST"])
@login_required
def AdminOnly():
    form = CardForm()
    if not current_user.role == "Admin":
        return redirect("/")
    if form.validate_on_submit():
        new_card = Shawarma(name=form.name.data, image=form.image.data.filename, information=form.information.data)
        db.session.add(new_card)
        db.session.commit()
        image = form.image.data
        image.save(f"{app.root_path}/static/{image.filename}")
    return render_template("Admin.html", form=form)

@app.route("/Registration", methods=["GET", "POST"])
def regisration():
    form = RegisterForm()
    if form.validate_on_submit():
        new_users = User(username=form.username.data, email=form.email.data, birth=form.birth.data, password=form.password.data, gender=form.gender.data)
        db.session.add(new_users)
        db.session.commit()
        print(new_users)
    return render_template("registration.html", form=form)


@app.route("/Login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_paasword(form.password.data):
            login_user(user)



    return render_template("Login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/info/<int:shawarma_id>")
def id(shawarma_id):
    return render_template("info.html", shawarma=Shawarma.query.get(shawarma_id))


@app.route("/post", methods=["GET", "POST"])
@login_required
def post():

    form = PostForm()
    if form.validate_on_submit():
        new_posts = Posts(username=current_user.username, text=form.post.data, photo=form.photo.data.filename)
        db.session.add(new_posts)
        db.session.commit()
        photo = form.photo.data
        photo.save(f"{app.root_path}/static/{photo.filename}")
    postebi = Posts.query.all()
    return render_template("post.html", form=form, postebi=postebi)






@app.route("/posts_detals/<int:posts_id>", methods=["GET", "POST"])
def id2(posts_id):
    form = CommentForm()
    post = Posts.query.get(posts_id)
    if form.validate_on_submit():
        new_comment = Comments(username=current_user.username, comment=form.comment.data, post_id=post.id)
        db.session.add(new_comment)
        db.session.commit()
    comments = Comments.query.filter_by(post_id=posts_id).all()
    return render_template("posts_detals.html", posti=post, form=form, comments=comments)
