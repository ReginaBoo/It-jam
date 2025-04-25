from flask import Blueprint, jsonify
from app.models import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        'id': user._id,
        'username': user.username,
        'preferredLanguage': user.preferredLanguage
    })
