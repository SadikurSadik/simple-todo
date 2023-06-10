from app import app
from flask import request, jsonify
import json
from apis.crud import insert, getData, delete, setRedisCache, getRedisCache, delRedisCache

from models import Todo

@app.route("/")
def index():
    return jsonify({'message': 'Hello from Flask API'})

@app.route("/create", methods=['POST'])
def postDataToDb():
    payload = request.get_json()
    value = payload['todo']
    if value:
        res = insert(value)
        delRedisCache()
        if res:
            return jsonify({"message":'Todo saved successfully'}), 201
    else:
        return jsonify({"message" : "todo field required"}), 400
    
@app.route("/data")
def getDatafromDB():
    data = []

    try:
        res = getRedisCache()
        if res:
            res = json.loads(res)
            return jsonify({'message' : 'success', 'isCached':'yes', 'data':res}), 200
        if res is None:
            res = getData()
            for i in res:
                data.append({ 'id': i.id, 'is_completed': i.is_completed, 'data':i.todo  })

            setRedisCache(json.dumps(data))
            return jsonify({'success' : True, 'isCached':'No', 'data': data}), 200
    except Exception as error:
        return jsonify({'success' : False, 'Error':type(error).__name__}), 400
    
@app.route("/delete/<int:id>", methods=['DELETE'])
def deleteDataToDb(id):
    if id:
        res = delete(id)
        delRedisCache()
        return jsonify({'success' : True, "message":'Todo deleted successfully'}), 201
    else:
        return jsonify({'success' : False, "message" : "todo deletion failed"}), 400