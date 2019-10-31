from get_metrics import *
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    response = ",".join(get_metrics(filename = "../bash/endpoints.json"))
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8000)
