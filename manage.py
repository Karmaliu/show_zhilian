from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from src.app import create_all, sql_db

app = create_all()
manager = Manager(app)
migrate = Migrate(app, sql_db)


def make_shell_context():
    return dict(app=app, db=sql_db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


@manager.command
def test():
    """run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def setup():
    print("start app init!!!")
    print("init successfuly ")


if __name__ == '__main__':
    manager.run(debug=True)
