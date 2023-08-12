from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

database = SQLAlchemy(app)


@app.route('/')
def home():
    return jsonify(message="Server running at port 8080")


if __name__ == '__main__':
    with app.app_context():
        database.create_all()  # Create the database tables within the application context
    app.run(debug=True, port=8080)  # Start the Flask server
