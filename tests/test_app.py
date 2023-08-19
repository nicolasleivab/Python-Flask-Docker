from main import create_app

app = create_app()


def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.json == {'message': 'Server running at port 8080'}


def test_get_messages():
    with app.test_client() as client:
        response = client.get('/get_messages')
        assert response.status_code == 200
        assert response.json == {'messages': []}


def test_add_message():
    with app.test_client() as client:
        response = client.post('/add_message', json={'content': 'Hello World'})
        assert response.status_code == 200
        assert response.json == {'message': 'Message added successfully'}

        response = client.get('/get_messages')
        assert response.status_code == 200
        assert response.json == {'messages': [
            {'id': 1, 'content': 'Hello World'}]}


def test_delete_message():
    # Adding a message to ensure there's something to delete
    with app.test_client() as client:
        response = client.post(
            '/add_message', json={'content': 'Temporary Message'})
        assert response.status_code == 200
        assert response.json == {'message': 'Message added successfully'}

        # Fetching messages to get the ID of the one we just added
        response = client.get('/get_messages')
        assert response.status_code == 200
        messages = response.json['messages']
        assert len(messages) > 0  # Ensure we have messages

        # Extracting the ID of the first message
        message_id = messages[0]['id']

        # Deleting the message using its id
        response = client.delete(f'/delete_message/{message_id}')
        assert response.status_code == 200
        assert response.json == {'message': 'Message deleted successfully'}

        # Verifying the deletion
        response = client.get('/get_messages')
        assert response.status_code == 200
        assert {'id': message_id,
                'content': 'Temporary Message'} not in response.json['messages']
