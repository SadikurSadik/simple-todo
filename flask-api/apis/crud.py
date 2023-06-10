from app import db
from models import Todo
from app import redis_db

CACHE_KEY = "all_todos"

def insert(data):
    todo = Todo(data)
    db.session.add(todo)
    db.session.commit()
    return todo

def getData():
    return Todo.query.all()

def delete(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return

def setRedisCache(data):
    redis_db.set(CACHE_KEY, data)
    return

def getRedisCache():
    return redis_db.get(CACHE_KEY)

def delRedisCache():
    redis_db.delete(CACHE_KEY)
    return