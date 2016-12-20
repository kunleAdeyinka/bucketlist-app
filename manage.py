from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
import os

from project import app, db


app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0',
    port= 8080)
)


if __name__ == '__main__':
    manager.run()