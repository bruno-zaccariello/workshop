from flask import Flask, jsonify
from flask import request as r

from database import database as db

app = Flask(__name__)

@app.route("/", methods=[])
def generic_function():
    # write sample code

if __name__ == "__main__":
    app.run(port:8080)
