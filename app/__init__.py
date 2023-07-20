from flask import Flask

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp

    app.register_blueprint(main_bp)

    from app.recordings import bp as recordings_bp

    app.register_blueprint(recordings_bp, url_prefix="/recordings")

    return app
