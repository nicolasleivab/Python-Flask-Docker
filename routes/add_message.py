from flask import jsonify, request
from main import database
from flask import current_app as app
from models.messages import Message


@app.route('/add_message', methods=['POST'])
def add_message():
    content = request.json.get('content')
    if content is None:
        return jsonify(error="Content is required"), 400

    new_message = Message(content=content)
    database.session.add(new_message)
    database.session.commit()

    return jsonify(message="Message added successfully")
