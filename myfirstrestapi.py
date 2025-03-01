from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector


app = Flask(__name__)

CORS(app)

db = mysql.connector.connect(
    host = "sql7.freesqldatabase.com",
    user = "sql7765008",
    password = "tGfmQAlvDa",
    database = "sql7765008",
    connection_timeout = 90
)

cursor = db.cursor()

db.commit()

@app.route("/news", methods=["GET"])
def get_users():
    cursor.execute("select * from newstest")
    news = cursor.fetchall()
    return jsonify([{"id":i[0], "title": i[1], "date": i[2], "text": i[3]} for i in news])



if __name__ == "__main__":
    app.run(debug=True, port = 5000)