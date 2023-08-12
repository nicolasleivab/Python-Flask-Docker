from flask import Flask, jsonify
from models.messages import db
from routes import register_routes

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db.init_app(app)


@app.route('/')
def home():
    return jsonify(message="Server running at port 8080")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables within the application context
        register_routes(app)
    app.run(debug=True, port=8080)  # Start the Flask server
