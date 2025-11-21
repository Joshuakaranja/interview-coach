# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register blueprints
    from app.routes.interview_routes import interview_bp
    app.register_blueprint(interview_bp)

    return app
