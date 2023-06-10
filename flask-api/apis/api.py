from app import app
from flask import request, jsonify
import json
from apis.crud import insert, getData, setRedisCache, getRedisCache, delRedisCache

@app.route("/")
def index():
    return "connected to app server"

@app.route("/create", methods=['POST'])
def postDataToDb():
    payload = request.get_json()
    value = payload['data']
    if value:
        res = insert(value)
        delRedisCache()
        if res:
            return jsonify({"message":'Data posted successfully'}), 201
    else:
        return jsonify({"message" : "Your field is empty"}), 400
    
@app.route("/data")
def getDatafromDB():
    data = []

    try:
        # res = getRedisCache()
        # if res:
        #     res = json.loads(res)
        #     return jsonify({'message' : 'success', 'isCached':'yes', 'data':res}), 200
        # if res is None:
            res = getData()
            for i in res:
                data.append({'data':i.data})

            setRedisCache(json.dumps(data))
            return jsonify({'success' : True, 'isCached':'No', 'data':data}), 200
    except Exception as error:
        return jsonify({'success' : False, 'Error':type(error).__name__}), 400