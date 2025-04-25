from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from werkzeug.security import generate_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    preferred_language = data.get('preferredLanguage', 'ru')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # Создание пользователя
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, passwordHash=hashed_password, preferredLanguage=preferred_language)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    # Логика для входа (например, проверка пароля и создание токена)
    return jsonify({'message': 'Login successful'}), 200
