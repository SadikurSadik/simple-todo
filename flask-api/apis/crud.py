from app import db
from models import Todo
from app import redis_db

CACHE_KEY = "all_todos"

def insert(data):
    variable = Todo(data)
    db.session.add(variable)
    db.session.commit()
    return variable

def getData():
    return Todo.query.all()

def setRedisCache(data):
    redis_db.set(CACHE_KEY, data)
    return

def getRedisCache():
    return redis_db.get(CACHE_KEY)

def delRedisCache():
    redis_db.delete(CACHE_KEY)
    return