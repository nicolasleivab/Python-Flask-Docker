from flask import Blueprint, jsonify
from models.messages import Message

get_messages_bp = Blueprint('get_messages', __name__)


@get_messages_bp.route('/get_messages')
def get_messages():
    messages = Message.query.all()
    message_list = [{'id': message.id, 'content': message.content}
                    for message in messages]
    return jsonify(messages=message_list)
