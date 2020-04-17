from flask_script import Manager
from views import app
from exts import db
from flask_migrate import Migrate, MigrateCommand
from models import User, Message

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()