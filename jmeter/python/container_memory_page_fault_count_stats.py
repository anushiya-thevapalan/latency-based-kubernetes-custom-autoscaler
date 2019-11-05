import json
#import objectpath
def get_container_memory_page_fault_count(filename, size, querying_factor):
    with open(filename) as datafile:
        data = json.load(datafile)

    #file = open("container_memory_page_fault_count_"+size+".csv", "w+")
    file = open(filename.replace("json", "csv"), "w+")

    header = ["pod_id", "cluster_name", "container_name", "instance_id", "startTime","endTime","fault_type","doubleValue"]
    file.write(",".join(string for string in header))
    file.write("\n")

    time_series = data.get("timeSeries")
    for metrics in time_series:
        resource = metrics.get("resource")
        # print(metrics.get("resource").get("labels").get("pod_id"))
        container_name = resource.get("labels").get("container_name")
        if (container_name.startswith(querying_factor)):
            pod_id = resource.get("labels").get("pod_id")
            cluster_name = resource.get("labels").get("cluster_name")
            instance_id = resource.get("labels").get("instance_id")
            fault_type = metrics.get("metric").get("labels").get("fault_type")

            points = metrics.get("points")
            for point in points:
                startTime = point.get("interval").get("startTime")
                endTime = point.get("interval").get("endTime")
                int64Value = point.get("value").get("int64Value")
                data = [pod_id,cluster_name,container_name, instance_id, str(startTime), str(endTime), fault_type, str(int64Value)]
                data = ",".join(string for string in data)
                file.write(data)
                file.write("\n")
    file.close()

# Testing purpose
# filename = "/home/anushiyat/Documents/wso2/project/server-architecture-performance/bash/container_memory_page_fault_count.json"
# get_container_memory_page_fault_count(filename)