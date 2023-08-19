# Python-Flask-Docker

Chat messages api built with python and flask.

### How to run Docker app

Make sure you have an instance of Docker running on your machine and run:

```
docker-compose up
```

[Troubleshooting Docker ERROR internal load metadata](https://stackoverflow.com/questions/66912085/why-is-docker-compose-failing-with-error-internal-load-metadata-suddenly/71665244#71665244)

### How to run locally (skip if using docker)

Install dependencies

```
pip3 install -r requirements.txt
```

Run local server

```
python3 main.py
```

### Add a chat message to add_message route

```
curl -X POST -H "Content-Type: application/json" -d '{"content": "Hi there!"}' http://localhost:5555/add_message
```

Check messages in the browser at [http://localhost:5555/get_messages](http://localhost:5555/get_messages)

### Remove message

```
curl -X DELETE http://localhost:5555/delete_message/1
```

### Stop container

```
docker-compose down
```

### Run tests in Docker by building test-service

```
docker-compose up --build test-service
```

### Run tests with local setup

```
coverage run -m pytest tests/test_app.py
```
