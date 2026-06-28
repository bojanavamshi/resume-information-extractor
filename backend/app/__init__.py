from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load config from environment
    app.config['SECRET_KEY'] = 'local_secret_key'
    app.config['UPLOAD_FOLDER'] = 'uploads/'

    # Import routes (local only)
    from backend import routes
    app.register_blueprint(routes.bp)

    return app