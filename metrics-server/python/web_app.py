from get_metrics import *
from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

@app.route("/")
def metrics():
    # response = get_metrics(filename = "../bash/endpoints.json")
    response = get_endpoints()
    response = {"latency" : response}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8000)
