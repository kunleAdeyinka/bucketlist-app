from app import db
from models import BlogPost


# cretae the database and the db tables
db.create_all()


# insert
db.session.add(BlogPost("Good", "I\'m good"))
db.session.add(BlogPost("Well", "I\'m well"))
db.session.add(BlogPost("Postgres", "I set up a local postgres instance"))


# commit the changes
db.session.commit()