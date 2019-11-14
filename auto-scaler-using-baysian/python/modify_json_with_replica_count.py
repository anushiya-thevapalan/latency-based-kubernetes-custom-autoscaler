import sys
import json
import os

filename = os.getcwd()+"/scale.json"
# filename = sys.argv[1]
required_pod_count = int(sys.argv[1])

print("Modifying required replica count to: ",required_pod_count)

def modify_pod_count(filename, pod_count):
    with open(filename, 'r') as datafile:
        data = json.load(datafile)
        data["spec"]["replicas"] = pod_count
    os.remove(filename)
    with open(filename, 'w') as datafile:
        json.dump(data, datafile, indent=4)

# filename = "scale.json"
# required_pod_count = 1
modify_pod_count(filename, required_pod_count)