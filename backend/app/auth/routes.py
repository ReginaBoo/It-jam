from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import mongo

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Проверка существования пользователя
    if mongo.db.users.find_one({'username': data['username']}):
        return jsonify({'error': 'Username already exists'}), 400
    
    # Хеширование пароля
    hashed_pw = generate_password_hash(data['password'])
    
    # Сохранение пользователя в MongoDB
    user = {
        'username': data['username'],
        'passwordHash': hashed_pw,
        'role': 'user',
        'preferredLanguage': data.get('preferredLanguage', 'ru')
    }
    mongo.db.users.insert_one(user)
    
    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = mongo.db.users.find_one({'username': data['username']})
    
    # Проверка пароля
    if not user or not check_password_hash(user['passwordHash'], data['password']):
        return jsonify({'error': 'Invalid username or password'}), 401
    
    # Генерация JWT-токена
    access_token = create_access_token(identity={
        'id': str(user['_id']),
        'username': user['username'],
        'role': user['role']
    })
    
    return jsonify({'access_token': access_token}), 200
