from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import redis

cors = CORS()
db = SQLAlchemy()

app = Flask(__name__)

#use os.get_env() and maintain .env file
# MySQL configuration
app.config['MYSQL_HOST'] = 'db'
# app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'simple_todo_db'

app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:12345678@host.docker.internal/simple_todo_db"

app.config['REDIS_HOST']="redis"
app.config['REDIS_PORT']=6379
redis_db = redis.Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])

cors.init_app(app)
db.init_app(app)

from apis import api