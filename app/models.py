from . import db 
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    psword = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.psword = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.psword,password)

    def __repr__(self):
        return f'User {self.username}'

    

        
class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    #writer = db.relationship()
    title = db.Column(db.String(255))
    content = db.Column(db.String())
    #comments = db.relationship()

    def __repr__(self):
        return f'Blog {self.content}'
