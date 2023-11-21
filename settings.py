import os


SECRET_KEY = os.getenv('SECRET_KEY')
DB_HOST=os.environ['DB_HOST']
DB_USERNAME=os.environ['DB_USERNAME']
DB_PASSWORD=os.environ['DB_PASSWORD']
DATABASE_NAME=os.environ['DATABASE_NAME']
DB_URI='postgresql://fahadtahir:flappy123@localhost:5432/counter'
SQLALCHEMY_DATABASE_URI = DB_URI