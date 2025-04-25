# Используем официальный образ Python
FROM python:3.9-slim

# Рабочая директория
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь бэкенд
COPY . .

# Запускаем сервер
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

# Открываем порт
EXPOSE 5000