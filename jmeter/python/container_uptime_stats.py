import json
#import objectpath
def get_container_uptime(filename, size, querying_factor):
    with open(filename) as datafile:
        data = json.load(datafile)

    #file = open("container_uptime_"+size+".csv", "w+")
    file = open(filename.replace("json", "csv"), "w+")

    header = ["pod_id", "cluster_name", "container_name", "instance_id", "startTime","endTime","doubleValue"]
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

            points = metrics.get("points")
            for point in points:
                startTime = point.get("interval").get("startTime")
                endTime = point.get("interval").get("endTime")
                doubleValue = point.get("value").get("doubleValue")
                data = [pod_id,cluster_name,container_name, instance_id, str(startTime), str(endTime), str(doubleValue)]
                data = ",".join(string for string in data)
                file.write(data)
                file.write("\n")
    file.close()

# Testing purpose
#filename = "/home/anushiyat/Documents/wso2/project/server-architecture-performance/container_uptime.json"
#get_container_uptime(filename,"1")
