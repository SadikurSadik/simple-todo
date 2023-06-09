from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

# Application instance
app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'host.docker.internal'
# app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test_db'

mysql = MySQL(app)


@app.route("/")
def hello():
    cur = mysql.connection.cursor() 
    cur.execute("""SELECT * FROM Users""")
    user = cur.fetchall()
    
    return jsonify(user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
