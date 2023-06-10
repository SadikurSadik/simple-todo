from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import redis

cors = CORS()
db = SQLAlchemy()

app = Flask(__name__)

#use os.get_env() and maintain .env file
# MySQL and Redis connection
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:password@db/simple_todo_db"

app.config['REDIS_HOST']="redis"
app.config['REDIS_PORT']=6379
redis_db = redis.Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])

cors.init_app(app)
db.init_app(app)

from apis import api