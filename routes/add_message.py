from flask import Blueprint, jsonify, request
from models.messages import Message
from models.messages import db

add_message_bp = Blueprint('add_message', __name__)


@add_message_bp.route('/add_message', methods=['POST'])
def add_message():
    content = request.json.get('content')
    if content is None:
        return jsonify(error="Content is required"), 400

    new_message = Message(content=content)
    db.session.add(new_message)
    db.session.commit()

    return jsonify(message="Message added successfully")
