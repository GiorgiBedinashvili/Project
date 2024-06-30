from ext import app, db
from models import Shawarma
from models import User, Posts, Comments

with app.app_context():
    db.create_all()


    admin_user = User("Admin", "ADMINPASSWORD123123","12/10/2009","admin@gmail.com", "male", "Admin")
    db.session.add(admin_user)
    db.session.commit()



