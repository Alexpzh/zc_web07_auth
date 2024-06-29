from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db' # Эта строчка нужна, чтобы мы могли подключиться к базе данных
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Эта строчка отключает сигнализацию об изменении объектов внутри базы данных
db = SQLAlchemy(app) # Создание объекта, через который мы будем работать с базой данных

