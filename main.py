from flask import Flask, jsonify
from models.messages import db
from routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.init_app(app)

    with app.app_context():
        db.create_all()
    register_routes(app)

    @app.route('/')
    def home():
        return jsonify(message="Server running at port 8080")

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8080)
