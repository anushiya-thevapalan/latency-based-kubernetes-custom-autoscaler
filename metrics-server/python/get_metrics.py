import json
import numpy as np
from get_server_metrics import *

def get_metrics(filename):
    metrics_of_all_pods = []
    latency_of_all_pods = []
    ip_address = get_replicas_ip(filename)

    for ip in ip_address:
        metrics = query_metrics(ip)
        metrics_of_all_pods.append()
        latency_of_all_pods.append(metrics["99per"])
    return get_cumulative_latency(latency_of_all_pods)

def get_cumulative_latency(latency_of_all_pods):
    return np.percentile(latency_of_all_pods,99)
    

def get_replicas_ip(filename):
    ip_address = []
    with open(filename, 'r') as datafile:
        data = json.load(datafile)
        test = data["subsets"][0]["addresses"]
        for i in test:
            ip_address.append(i["ip"])
    return ip_address

#def get_endpoints()
filename = "../bash/endpoints.json"
get_metrics(filename)