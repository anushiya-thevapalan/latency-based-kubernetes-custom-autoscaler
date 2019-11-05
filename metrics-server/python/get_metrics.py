import json
import subprocess
import time
import csv
import os
#import numpy as np
from get_server_metrics import *

def get_metrics(filename):
    metrics_of_all_pods = []
    latency_of_all_pods = []
    ip_address = get_replicas_ip(filename)

    time_now = time.time()

    latency_stats_file = "/home/metrics-server/python/latency_stats.csv"

    for ip in ip_address:
        metrics = query_metrics(ip)
        metrics["timestamp"] = time_now
        print(metrics)
        metrics_of_all_pods.append(metrics)
        print(metrics["99per"])
        latency_of_all_pods.append(metrics["99per"])
    average_latency = get_average_latency(latency_of_all_pods)

    if not os.path.isfile(latency_stats_file):
        print("creating file")
        with open(latency_stats_file, "a+") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            headers = ['Timestamp', 'Average_latency', 'Number_of_pods']
            writer.writerow(headers)

    with open(latency_stats_file, "a+") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        values =  [time_now, average_latency, len(ip_address)] 
        writer.writerow(values)

    return average_latency

def get_average_latency(latency_of_all_pods):
    # x = np.percentile(latency_of_all_pods,99)
    return sum(latency_of_all_pods)/len(latency_of_all_pods)
    

def get_replicas_ip(filename):
    ip_address = []
    with open(filename, 'r') as datafile:
        data = json.load(datafile)
        test = data["subsets"][0]["addresses"]
        for i in test:
            ip_address.append(i["ip"])
    return ip_address

#Main function to be called
def get_endpoints():
    subprocess.call(['../bash/test.sh'])
    filename = "../bash/endpoints.json"
     
    return get_metrics(filename)