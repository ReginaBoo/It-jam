from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)

    # Импорты ВНУТРИ функции, чтобы избежать циклических импортов
    from app.routes.auth import auth_bp
    from app.routes.users import users_bp
    from app.routes.places import places_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(places_bp, url_prefix='/api/places')

    return app
