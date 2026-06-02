# Basic Authentication

A Flask API with Basic Authentication implementation.

## Files

### `models/`
- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`
- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status`, `/stats`, `/unauthorized`, `/forbidden`
- `views/users.py`: all users endpoints
- `auth/auth.py`: base Auth class
- `auth/basic_auth.py`: BasicAuth class implementing Basic Authentication

## Setup

```
pip3 install -r requirements.txt
```

## Run

```
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
```

## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/unauthorized`: raises a 401 error
- `GET /api/v1/forbidden`: raises a 403 error
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns a user based on the ID
- `DELETE /api/v1/users/:id`: deletes a user based on the ID
- `POST /api/v1/users`: creates a new user
- `PUT /api/v1/users/:id`: updates a user based on the ID
