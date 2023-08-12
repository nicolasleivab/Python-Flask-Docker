from main import app
from routes import register_routes

register_routes(app)  # Register the routes with the app


def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.json == {'message': 'Server running at port 8080'}


# def test_get_messages():
#     with app.test_client() as client:
#         response = client.get('/get_messages')
#         assert response.status_code == 200
#         assert response.json == {'messages': []}


# def test_add_message():
#     with app.test_client() as client:
#         response = client.post('/add_message', json={'content': 'Hello World'})
#         assert response.status_code == 200
#         assert response.json == {'message': 'Message added successfully'}

#         response = client.get('/get_messages')
#         assert response.status_code == 200
#         assert response.json == {'messages': [
#             {'id': 1, 'content': 'Hello World'}]}
