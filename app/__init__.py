from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_migrate import Migrate

from app.config import Config


db = SQLAlchemy()

login_manager = LoginManager()

socketio = SocketIO()

migrate = Migrate()


def create_app():

    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    login_manager.init_app(app)

    socketio.init_app(
    app,
    cors_allowed_origins="*",
    async_mode="threading"
)

    login_manager.login_view = "auth.login"

    from app.routes import routes
    from app.auth import auth
    from app import socket_events

    app.register_blueprint(routes)

    app.register_blueprint(auth)

    return app