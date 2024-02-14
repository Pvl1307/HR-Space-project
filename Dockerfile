FROM python:3.10

# Установка Node.js и npm
RUN apt-get update && \
    apt-get install -y nodejs npm && \
    npm install -g n && \
    n 14

# Устанавливаем рабочую директорию
WORKDIR /code

# Копируем файлы Python
COPY pyproject.toml .

# Устанавливаем зависимости Python
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev --no-root

# Копируем файлы React
COPY ./react/ /code/react

# Устанавливаем зависимости React и собираем проект
WORKDIR /code/react
RUN npm install && npm run build

# Возвращаемся в основную директорию
WORKDIR /code

# Копируем все остальные файлы
COPY . .
