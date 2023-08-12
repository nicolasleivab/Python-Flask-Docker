# Python-Flask-Docker

Chat messages api built with python and flask.

### How to run locally

Install dependencies

```
pip3 install -r requirements.txt
```

Run local server

```
python3 main.py
```

Add a chat message to add_message route

```
curl -X POST -H "Content-Type: application/json" -d '{"content": "Hello, world!"}' http://localhost:8080/add_message
```

Check messages in the browser at [http://localhost:8080/get_messages](http://localhost:8080/get_messages)
