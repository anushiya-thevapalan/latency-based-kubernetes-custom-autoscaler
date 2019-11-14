#Script to be used when running a single jmx file
backend_host_ip=35.226.188.246

#Running on a server - comment it when running on my pc
jmeter_jtl_location=/home/jmeter/jtls
jmeter_jmx_file_root=/home/jmeter/jmx
server_metrics_location=/home/jmeter/server-metrics

jmeter_jtl_splitter_jar_file=/home/jmeter/jar/jtl-splitter-0.3.1-SNAPSHOT.jar

jmeter_performance_report_python_file=/home/jmeter/python/performance-report.py
jmeter_performance_report_output_file=/home/jmeter/results.csv

server_performance_report_generation_python_file=/home/jmeter/python/collect-metrics.py

#Running on my pc -comment it when running on server
# jmeter_jtl_location=/home/anushiyat/Documents/wso2/project/latency-based-kubernetes-custom-autoscaler/jmeter/jtls
# jmeter_jmx_file_root=/home/anushiyat/Documents/wso2/project/latency-based-kubernetes-custom-autoscaler/jmeter/jmx
# server_metrics_location=/home/anushiyat/Documents/wso2/project/latency-based-kubernetes-custom-autoscaler/jmeter/server-metrics

# jmeter_jtl_splitter_jar_file=/home/anushiyat/Documents/wso2/project/latency-based-kubernetes-custom-autoscaler/jmeter/jar/jtl-splitter-0.3.1-SNAPSHOT.jar

# jmeter_performance_report_python_file=/home/anushiyat/Documents/wso2/project/latency-based-kubernetes-custom-autoscaler/jmeter/python/performance-report.py
# jmeter_performance_report_output_file=/home/anushiyat/Documents/wso2/project/latency-based-kubernetes-custom-autoscaler/jmeter/results.csv

# server_performance_report_generation_python_file=/home/anushiyat/Documents/wso2/project/latency-based-kubernetes-custom-autoscaler/jmeter/python/collect-metrics.py

rm -r ${jmeter_jtl_location}/
rm -r ${server_metrics_location}/

mkdir -p ${jmeter_jtl_location}/
mkdir -p ${server_metrics_location}/

concurrent_users=(5)
heap_sizes=(100m)
garbage_collectors=(UseParallelGC)
use_case=prime
request_timeout=50000

size=10000019

start_time=$(date +%Y-%m-%dT%H:%M:%S.%N)
echo "start time : "${start_time}

jmeter -n -t ${jmeter_jmx_file_root}/varying_concurrency.jmx -l ${jmeter_jtl_location}/results.jtl

end_time=$(date +%Y-%m-%dT%H:%M:%S.%N)
echo "end time : "${end_time}

				
			
