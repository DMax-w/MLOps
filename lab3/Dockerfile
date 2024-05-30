# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем переменные окружения
ENV IRIS_SCALER=./model_dump/iris_scaler.pkl
ENV IRIS_MODEL=./model_dump/iris_model.pkl

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости
COPY ./src/app/requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r ./requirements.txt

# Копируем код приложения
COPY ./src/app .

# Копируем дамп модели
COPY ./src/model_dump ./model_dump

# Запускаем приложение
ENTRYPOINT ["streamlit", "run", "./app.py", "--server.port", "7070"]
