# app/routes.py
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Проверка существования пользователя в базе данных SQLite
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    
    # Хеширование пароля
    hashed_pw = generate_password_hash(data['password'])
    
    # Сохранение пользователя в базе данных SQLite
    user = User(
        username=data['username'],
        passwordHash=hashed_pw,
        role='user',  # Роль по умолчанию 'user'
        preferredLanguage=data.get('preferredLanguage', 'ru')  # Роль по умолчанию 'ru'
    )
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully'}), 201
# app/routes.py
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Поиск пользователя в базе данных SQLite
    user = User.query.filter_by(username=data['username']).first()
    
    # Проверка пароля
    if not user or not check_password_hash(user.passwordHash, data['password']):
        return jsonify({'error': 'Invalid username or password'}), 401
    
    # Генерация JWT-токена
    access_token = create_access_token(identity={
        'id': user._id,
        'username': user.username,
        'role': user.role
    })
    
    return jsonify({'access_token': access_token}), 200