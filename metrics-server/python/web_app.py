# from get_metrics import *
# from flask import Flask

# import requests

# app = Flask(__name__)

# URL="https://kubernetes/api/v1/namespaces/default/endpoints/ballerina-prime-testing-svc"
# token_file_path="/var/run/secrets/kubernetes.io/serviceaccount/token"
# ca_cert="/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"

# with open('data.txt', 'r') as file:
#     token = file.read()

# headers = {'Accept': 'application/json', "Authorization": "Bearer "+token}

# @app.route("/")
# def hello():
#     res = requests.get(url=URL, headers=headers, verify=ca_cert)
#     response = get_metrics(filename = "../bash/endpoints.json")
#     response = {"latency" : response}
#     return response

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port= 8000)


from get_metrics import *
from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

@app.route("/")
def hello():
    # response = get_metrics(filename = "../bash/endpoints.json")
    response = get_endpoints()
    response = {"latency" : response}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8000)
