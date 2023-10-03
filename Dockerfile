FROM ubuntu:latest
LABEL authors="ramisbariev"

# Используйте официальный образ Python как родительский образ
FROM python:3.11

# Установите рабочий каталог в контейнере
WORKDIR /home/ramisbariev/PycharmProjects/test

# Скопируйте файлы проекта в рабочий каталог
COPY . .

# Установите любые необходимые зависимости, указанные в requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Возможно, вам потребуется установить некоторые системные зависимости
# RUN apt-get update && apt-get install -y your-system-dependencies

# Запускайте ваше приложение при запуске контейнера
CMD [ "python", "./main.py" ]

ENTRYPOINT ["top", "-b"]