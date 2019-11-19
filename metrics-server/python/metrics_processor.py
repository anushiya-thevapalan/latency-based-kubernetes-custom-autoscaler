import json
import subprocess
import time
import csv
import os
import datetime
from metrics_collector import *

#Files to which metrics should be logged
latency_stats_file = "/home/metrics-server/python/latency_stats.csv"
latency_of_all_pods_file = "/home/metrics-server/python/latency_of_all_pods_file.csv"

time_now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

def get_metrics():

    ip_address = get_replicas_ip()
    latency_of_all_pods = []

    #Collecting metrics from individual pods
    for ip in ip_address:
        metrics = query_metrics(ip)
        print(metrics)

        #Logging metrics of  each pod to a file
        with open(latency_of_all_pods_file, "a+") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            values =  [ip, time_now, metrics["99per"], metrics["requests"], metrics["std_dev"]] 
            writer.writerow(values)
                
        latency_of_all_pods.append(metrics["99per"])
    average_latency = get_average_latency(latency_of_all_pods)

    #Logging average latency to a file
    with open(latency_stats_file, "a+") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        values =  [time_now, average_latency, len(ip_address)] 
        writer.writerow(values)

    return average_latency

def get_replicas_ip():
    ip_address = []
    subprocess.call(['../bash/get_endpoints.sh'])
    filename = "../bash/endpoints.json"

    with open(filename, 'r') as datafile:
        data = json.load(datafile)
        address = data["subsets"][0]["addresses"]
        for i in address:
            ip_address.append(i["ip"])
    return ip_address

#Compute average latency of all pods
def get_average_latency(latency_of_all_pods):
    return sum(latency_of_all_pods)/len(latency_of_all_pods)