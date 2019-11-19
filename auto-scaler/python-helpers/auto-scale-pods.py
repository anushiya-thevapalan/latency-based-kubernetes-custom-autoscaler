import os
import json
import requests
import sys

from desired_pod_cal import *

latency_response = sys.argv[1]
latency_response = json.loads(latency_response)

desired_latency = int(sys.argv[2])
min_pod = int(sys.argv[3])
max_pod = int(sys.argv[4])
filename = sys.argv[5]
# desired_latency = 5000
# min_pod = 1
# max_pod = 20
# filename = os.getcwd()+"/scale.json"

#metrics_url = "http://10.32.1.24:8000"

#function to be used when extrating metrics from monitoring pod
def auto_scale():
    current_latency = float(latency_response["latency"])
    current_pod_count = get_current_pod_count()
    #current_latency = float(requests.get(url=metrics_url))

    desired_pod = compute_desired_pods(current_latency, desired_latency, current_pod_count, min_pod, max_pod)
    print("Desired pods", desired_pod)

    set_pod_count(desired_pod)

def get_current_pod_count():
    with open(filename, 'r') as datafile:
        data = json.load(datafile)
        current_pod_count = int(data["spec"]["replicas"] )
        print("Current pods", current_pod_count)
    return current_pod_count

def set_pod_count(pod_count):
    with open(filename, 'r') as datafile:
        data = json.load(datafile)
        # data["spec"]["replicas"] = pod_count
    data["spec"]["replicas"] = pod_count
    # os.remove(filename)
    with open(filename, 'w') as datafile:
        json.dump(data, datafile, indent=4)

auto_scale()