import sqlite3

# Подключаемся к базе данных (если она не существует, будет создана)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создаем таблицу User
cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    passwordHash TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('user', 'moderator', 'admin')),
    preferredLanguage TEXT CHECK(preferredLanguage IN ('ru', 'en'))
)
''')

# Создаем таблицу Place
cursor.execute('''
CREATE TABLE IF NOT EXISTS Place (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    lat REAL NOT NULL,
    lng REAL NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('cafe', 'pharmacy', 'atm', 'landmark')),
    description TEXT,
    createdBy INTEGER NOT NULL,
    status TEXT CHECK(status IN ('pending', 'approved', 'rejected')),
    FOREIGN KEY (createdBy) REFERENCES User (_id)
)
''')

# Создаем таблицу Review
cursor.execute('''
CREATE TABLE IF NOT EXISTS Review (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    placeId INTEGER NOT NULL,
    userId INTEGER NOT NULL,
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    text TEXT,
    photos TEXT,  -- В SQLite можно хранить фотографии как текст (например, ссылки)
    likes TEXT,  -- Лайки можно хранить как список пользователей в формате строк
    status TEXT CHECK(status IN ('pending', 'approved', 'rejected')),
    createdAt TEXT NOT NULL,  -- Дата и время отзыва
    FOREIGN KEY (placeId) REFERENCES Place (_id),
    FOREIGN KEY (userId) REFERENCES User (_id)
)
''')

# Создаем таблицу Favorite
cursor.execute('''
CREATE TABLE IF NOT EXISTS Favorite (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER NOT NULL,
    lat REAL NOT NULL,
    lng REAL NOT NULL,
    FOREIGN KEY (userId) REFERENCES User (_id)
)
''')

# Сохраняем изменения
conn.commit()

# Закрываем соединение с базой данных
conn.close()

print("База данных и таблицы успешно созданы.")
