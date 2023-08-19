from flask import Blueprint

from .get_messages import get_messages_bp
from .add_message import add_message_bp
from .delete_message import delete_message_bp


def register_routes(app):
    # Notice the url_prefix
    app.register_blueprint(get_messages_bp, url_prefix='/')
    app.register_blueprint(add_message_bp, url_prefix='/')
    app.register_blueprint(delete_message_bp, url_prefix='/')
