from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.config import Config
import os
from pathlib import Path

# Инициализация экземпляров
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # Загрузка конфигурации
    app.config.from_object(Config)
    
    # Убедимся, что папка instance существует
    instance_path = Path(app.instance_path)
    instance_path.mkdir(exist_ok=True)
    
    # Проверка доступности пути БД
    db_path = Path(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', ''))
    try:
        db_path.parent.mkdir(exist_ok=True, parents=True)
    except Exception as e:
        app.logger.error(f"Cannot create database directory: {e}")
        raise
    
    # Инициализация расширений
    db.init_app(app)
    jwt.init_app(app)
    
    # Создание таблиц при первом запуске
    with app.app_context():
        try:
            db.create_all()
            app.logger.info("Database tables created successfully")
        except Exception as e:
            app.logger.error(f"Database creation error: {e}")
            raise
    
    # Регистрация маршрутов
    from app import routes
    app.register_blueprint(routes.auth_bp, url_prefix='/api')
    
    return app