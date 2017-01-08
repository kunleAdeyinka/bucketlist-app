from project import db
from project import bcrypt


from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


        
class User(db.Model):
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    bucketitems = relationship("BucketItem", backref="author")
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        
    def is_authenticated(self):
        return True
        
    def is_active(self):
        return True
        
    def get_id(self):
        return unicode(self.id)
        
    def is_anonymous(self):
        return False
        
    def __repr__(self):
        return '<name - {}>'.format(self.name)


class BucketItem(db.Model):
    
    __tablename__ = "bucketitems"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    post = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('users.id'))
    
    def __init__(self, title, post, author_id):
        self.title = title
        self.post = post
        self.author_id = author_id
        
    def __repr__(self):
        return '<title {}'.format(self.title)
    