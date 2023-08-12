from main import database


class Message(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    content = database.Column(database.String(255))
