from app import create_app, db

from app.models import User, Place

app = create_app()

if __name__ == '__main__':
    # Создание базы данных при первом запуске
    with app.app_context():
        db.create_all()
    app.run(debug=True)
