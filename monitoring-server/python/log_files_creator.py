import csv
import os

latency_stats_file = "/home/monitoring-server/python/latency_stats.csv"
latency_of_all_pods_file = "/home/monitoring-server/python/latency_of_all_pods_file.csv"


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