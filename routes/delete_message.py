from flask import Blueprint, jsonify
from models.messages import Message
from models.messages import db

delete_message_bp = Blueprint('delete_message', __name__)


@delete_message_bp.route('/delete_message/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = Message.query.get(message_id)

    if not message:
        return jsonify(error="Message not found"), 404

    db.session.delete(message)
    db.session.commit()

    return jsonify(message="Message deleted successfully")
