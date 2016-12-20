from project import db
from project.models import User

# inserts the data into the database
#db.session.add(User("john", "john@example.com", "johnnyboy"))
#db.session.add(User("admin", "admin@example.com", "admin"))
db.session.add(User("test", "test@example.com", "test"))


# commit the changes to the user table in the database
db.session.commit()