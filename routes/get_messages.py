from flask import jsonify, request
from flask import current_app as app  # Import the current_app object
from models.messages import Message


@app.route('/get_messages')
def get_messages():
    messages = Message.query.all()
    message_list = [{'id': message.id, 'content': message.content}
                    for message in messages]
    return jsonify(messages=message_list)
