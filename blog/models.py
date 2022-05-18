from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from blog import db, login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))   #7:30


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    username = db.Column(db.String(12), unique=True, nullable=False)
    email = db.Column(db.String(50), default=username + '@gmail.com')
    password = db.Column(db.String(250), nullable=False)
    role = db.Column(db.String(20), default="Testimonial")
    theme = db.Column(db.String(5), default="Light")
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    folders = db.relationship('Folder', backref='author', lazy='dynamic')
    cit = db.relationship('Cit', backref='author', lazy='dynamic')

    def __repr__(self):
        return f"User('{ self.id }', '{ self.username }', '{ self.email }')"

    def set_password_hash(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    title = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(250))
    description = db.Column(db.String(240))
    body = db.Column(db.Text(), nullable=False)
    body2 = db.Column(db.Text())
    body3 = db.Column(db.Text())
    body4 = db.Column(db.Text())
    body5 = db.Column(db.Text())
    cit = db.Column(db.Text())
    cit2 = db.Column(db.Text())
    cit3 = db.Column(db.Text())
    image = db.Column(db.String(120))

    def __repr__(self):
        return f"Post('{ self.id }', '{ self.title }')"

class Folder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    title = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(250))
    description = db.Column(db.String(240))
    cover = db.Column(db.String(120))
    media = db.Column(db.String(120))

    def __repr__(self):
        return f"Post('{ self.id }', '{ self.title }')"

class Cit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    slug = db.Column(db.String(250))
    body = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"Post('{ self.id }', '{ self.title }')"