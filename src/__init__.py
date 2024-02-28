from flask import Flask

from src.models import db, User
from src.config import Config
from src.commands import init_db, populate_db
from src.extensions import login_manager
from src.admin import admin


COMMANDS = [init_db, populate_db]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_commands(app)

    @app.route("/")
    def initial():
        return "Hello world!"

    return app


def register_extensions(app):

    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get_or_404(user_id)

    # Flask-Admin
    admin.init_app(app)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
