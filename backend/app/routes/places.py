from flask import Blueprint, jsonify
from app.models import Place

places_bp = Blueprint('places', __name__)

@places_bp.route('/<int:place_id>', methods=['GET'])
def get_place(place_id):
    place = Place.query.get_or_404(place_id)
    return jsonify({
        'name': place.name,
        'address': place.address,
        'lat': place.lat,
        'lng': place.lng,
        'type': place.type,
        'description': place.description
    })
