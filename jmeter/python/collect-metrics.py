# importing the requests library
import time, re, sys
import requests, schedule

# importing the URL % encoding library
import urllib
# importing datetime to get the timestamp
import datetime
from container_cpu_usage_time import *
from container_cpu_utilization_stats import *
from container_memory_bytes_total_stats import *
from container_memory_bytes_used_stats import *
from container_memory_page_fault_count_stats import *
from container_uptime_stats import *

output_folder = sys.argv[1]
start_time = sys.argv[2]
end_time = sys.argv[3]
size = sys.argv[4]
concurrency = sys.argv[5]


def query_metrics(output_folder, start_time, end_time, size, concurrency):
    try:
        # python 2
        # start_time = urllib.quote(start_time, safe='')
        # python3
        start_time = urllib.parse.quote(start_time, safe='')

        end_time = urllib.parse.quote(end_time, safe='')
        filenames = []

        # container_metrics_list = ["container/cpu/usage_time", "container/cpu/utilization", "container/memory/bytes_total",
        #                 "container/memory/bytes_used", "container/memory/page_fault_count", "container/uptime"]
        container_metrics_list = ["container/cpu/utilization"]
        headers = {
            'Authorization': 'Bearer [OAuth 2.0 access token]'}

        for metrics in container_metrics_list:
            # file = open(str(time.time()), "a")
            filename = output_folder+"/"+metrics.replace("/", "_")+"_"+size+"_"+concurrency+".json"
            filenames.append(filename)

            file = open(filename, "w+")

            #Add the API key at the end of the URL
            URL = "https://monitoring.googleapis.com/v3/projects/auto-scaling-springboot/timeSeries?filter=metric.type%20%3D%20%22container.googleapis.com%2F"+urllib.parse.quote(metrics, safe='')+"%22%20&interval.endTime=" + end_time + "Z&interval.startTime=" + start_time + "Z&key=[API key]"
            response = requests.get(url=URL, headers=headers)

            data = response.text

            file.write(data)
            file.close()

        pod_name = "ballerina-prime-testing"
        # get_container_cpu_usage(filename=filenames[0], size=size, querying_factor=pod_name)
        get_container_cpu_utilization(filename=filenames[0], size=size, querying_factor=pod_name)
        # get_container_memory_bytes_total(filename=filenames[2], size=size, querying_factor=pod_name)
        # get_container_memory_bytes_used(filename=filenames[3], size=size, querying_factor=pod_name)
        # get_container_memory_page_fault_count(filename=filenames[4], size=size, querying_factor=pod_name)
        # get_container_uptime(filename=filenames[5], size=size, querying_factor=pod_name)


    except Exception as e:
        print(e)
#Testing purpose
# output_folder = "/home/anushiyat/Documents/wso2/project/server-architecture-performance/"
# start_time = '2019-09-09T04:42:45.615723941'
# end_time = '2019-09-09T04:45:45.615723941'
# size = "521"
# concurrency = "10"
# schedule.every(1).minute.do(query_metrics(start_time, end_time))
query_metrics(output_folder, start_time, end_time, size, concurrency)

# while True:
#    schedule.run_pending()
#    #print("waiting")
#    time.sleep(1)
