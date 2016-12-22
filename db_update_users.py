from project import db
from project.models import User
from project.models import bcrypt

user1 = User.query.filter_by(name='admin').first()
password = bcrypt.generate_password_hash(user1.password)
user1.password = password
db.session.commit()

user2 = User.query.filter_by(name='john').first()
password = bcrypt.generate_password_hash(user2.password)
user2.password = password
db.session.commit()


user3 = User.query.filter_by(name='test').first()
password = bcrypt.generate_password_hash(user3.password)
user3.password = password
db.session.commit()