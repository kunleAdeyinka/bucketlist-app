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
    bucketitems = relationship("BucketItem", backref="author", lazy='dynamic')
    likes = db.relationship('Like', backref='user', lazy='dynamic')
    
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
    description = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('users.id'))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    photo_path = db.Column(db.String,nullable=True)
    is_private = db.Column(db.Boolean, default=False)
    is_done = db.Column(db.Boolean, default=False)
    
    
    likes = db.relationship('Like', backref='bucketitem', lazy='dynamic')
    
    def __init__(self, title, description, author_id, is_private, is_done, photo_path):
        self.title = title
        self.description = description
        self.author_id = author_id
        self.is_private = is_private
        self.is_done = is_done
        self.photo_path = photo_path
        
    def __repr__(self):
        return '<title {}'.format(self.title)
        
class Like(db.Model):
    
    __tablename__ = "likes"
    
    id = db.Column(db.Integer, primary_key=True)
    bucketitem_id = db.Column(db.Integer, db.ForeignKey('bucketitems.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    likes = db.Column(db.Integer,default=0)
    
    
    
    def __init__(self, bucketitem_id, user_id, likes):
        self.bucketitem_id = bucketitem_id
        self.user_id = user_id
        self.likes = likes
        
    def __repr__(self):
        return '<title {}, {}'.format(self.bucketitem_id, self.likes)
