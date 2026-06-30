from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.update(SECRET_KEY="local_secret_key", UPLOAD_FOLDER="uploads/")
    return app
