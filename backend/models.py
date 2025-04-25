from app import db  # Импортируем db из приложения
print(db)
from sqlalchemy import CheckConstraint

class User(db.Model):
    __tablename__ = 'User'

    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    passwordHash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    preferredLanguage = db.Column(db.String(2))

class Place(db.Model):
    __tablename__ = 'Place'

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    createdBy = db.Column(db.Integer, db.ForeignKey('User._id'))
    status = db.Column(db.String(50), nullable=False)
    
    __table_args__ = (
        CheckConstraint('type IN ("cafe", "pharmacy", "atm", "landmark")', name='check_type'),
        CheckConstraint('status IN ("pending", "approved", "rejected")', name='check_status'),
    )

class Review(db.Model):
    __tablename__ = 'Review'

    _id = db.Column(db.Integer, primary_key=True)
    placeId = db.Column(db.Integer, db.ForeignKey('Place._id'))
    userId = db.Column(db.Integer, db.ForeignKey('User._id'))
    rating = db.Column(db.Integer)
    text = db.Column(db.Text)
    photos = db.Column(db.Text)
    likes = db.Column(db.Text)
    status = db.Column(db.String(50))
    createdAt = db.Column(db.String(20))

class Favorite(db.Model):
    __tablename__ = 'Favorite'

    _id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('User._id'))
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
