import json
import subprocess
import time
import csv
import os
import datetime
from metrics_collector import *

latency_stats_file = "/home/metrics-server/python/latency_stats.csv"
latency_of_all_pods_file = "/home/metrics-server/python/latency_of_all_pods_file.csv"

time_now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

def get_endpoints():
    subprocess.call(['../bash/get_endpoints.sh'])
    return 

def get_replicas_ip(filename):
    ip_address = []
    with open(filename, 'r') as datafile:
        data = json.load(datafile)
        test = data["subsets"][0]["addresses"]
        for i in test:
            ip_address.append(i["ip"])
    return ip_address

def get_average_latency(latency_of_all_pods):
    # x = np.percentile(latency_of_all_pods,99)
    return sum(latency_of_all_pods)/len(latency_of_all_pods)

def create_log_files():
    if not os.path.isfile(latency_of_all_pods_file):
        print("creating file")
        with open(latency_of_all_pods_file, "a+") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            headers = ['Pod_IP','Timestamp', 'Average_latency', 'requests', 'std_dev']
            writer.writerow(headers)

    if not os.path.isfile(latency_stats_file):
        print("creating file")
        with open(latency_stats_file, "a+") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            headers = ['Timestamp', 'Average_latency', 'Number_of_pods']
            writer.writerow(headers)


get_endpoints()
filename = "../bash/endpoints.json"

ip_address = get_replicas_ip(filename)
latency_of_all_pods = []

for ip in ip_address:
    metrics = query_metrics(ip)
    metrics["timestamp"] = time_now
    print(metrics)
        
    with open(latency_of_all_pods_file, "a+") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        values =  [ip, time_now, metrics["99per"], metrics["requests"], metrics["std_dev"]] 
        writer.writerow(values)
            
    # metrics_of_all_pods.append(metrics)
    print(metrics["99per"])
    latency_of_all_pods.append(metrics["99per"])
average_latency = get_average_latency(latency_of_all_pods)

with open(latency_stats_file, "a+") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    values =  [time_now, average_latency, len(ip_address)] 
    writer.writerow(values)