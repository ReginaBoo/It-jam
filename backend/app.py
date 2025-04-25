from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app/data/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Новый стиль инициализации для Flask-SQLAlchemy 3.x
db = SQLAlchemy()
db.init_app(app)

class Place(db.Model):
    __tablename__ = 'places'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

@app.route('/api/places')
def get_places():
    with app.app_context():  # Обязательно для Flask-SQLAlchemy 3.x
        places = db.session.execute(db.select(Place)).scalars()
        return jsonify([{'name': p.name, 'lat': p.lat, 'lng': p.lng} for p in places])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0')