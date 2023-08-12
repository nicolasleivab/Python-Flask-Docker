from flask import Blueprint

from .get_messages import get_messages_bp
from .add_message import add_message_bp


def register_routes(app):
    app.register_blueprint(get_messages_bp)
    app.register_blueprint(add_message_bp)
