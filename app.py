# app.py
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from yourapp.extensions import db, migrate
from yourapp.views.users import users_bp
from yourapp.views.posts import posts_bp

def create_app(config_object=None):
    app = Flask(__name__, instance_relative_config=True)
    # Load config
    app.config.from_object(config_object or os.getenv('FLASK_CONFIG', 'yourapp.config.DevelopmentConfig'))

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(posts_bp, url_prefix='/posts')

    # Root health-check
    @app.route('/')
    def index():
        return jsonify({"status": "ok", "msg": "Welcome to the API!"})

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

