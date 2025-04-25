from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from sqlalchemy import inspect  # Импортируем inspect
from models import User, Place, Review, Favorite  # Импортируем ваши модели

# Инициализация приложения Flask
app = Flask(__name__)
app.config.from_object(Config)  # Загружаем настройки из config.py

# Инициализация SQLAlchemy
db = SQLAlchemy()
db.init_app(app)  # Инициализируем SQLAlchemy с приложением Flask

@app.route('/')
def index():
    return "Hello, World!"

# Создание таблиц в контексте приложения
with app.app_context():
    db.create_all()  # Создаём все таблицы для моделей

    # Проверим, что таблицы созданы
    inspector = inspect(db.engine)  # Создаем инспектор для работы с базой данных
    tables = inspector.get_table_names()  # Получаем список всех таблиц в базе данных
    print("Таблицы в базе данных:", tables)

@app.route('/add_places')
def add_places():
    # Добавление тестовых данных в таблицу Place

   
    place1 = Place(
        name="Central Park", 
        address="New York, NY", 
        lat=40.785091, 
        lng=-73.968285, 
        type="cafe", 
        description="A large public park in New York City", 
        createdBy=1,  # ID пользователя, предполагаем, что это пользователь с ID=1
        status="pending"
    )
    
    place2 = Place(
        name="Eiffel Tower", 
        address="Champ de Mars, 5 Avenue Anatole", 
        lat=48.8588443, 
        lng=2.2943506, 
        type="cafe", 
        description="An iron lattice tower on the Champ de Mars in Paris, France", 
        createdBy=1,  # ID пользователя
        status="pending"
    )
    
    # Добавляем их в сессию базы данных и сохраняем
    db.session.add(place1)
    db.session.add(place2)
    db.session.commit()  # Сохраняем изменения в базе

    return "Test places added successfully!"

@app.route('/api/places')
def get_places():
    with app.app_context():  # Обязательно для Flask-SQLAlchemy 3.x
        places = db.session.execute(db.select(Place)).scalars()
        return jsonify([{
            'name': p.name,
            'address': p.address,
            'lat': p.lat,
            'lng': p.lng,
            'type': p.type,
            'description': p.description,
            'createdBy': p.createdBy,
            'status': p.status
        } for p in places])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создаём все таблицы для моделей
    app.run(host='0.0.0.0', debug=True)
