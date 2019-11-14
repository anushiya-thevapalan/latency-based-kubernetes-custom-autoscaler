jmeter_jtl_splitter_jar_file=/home/anushiyat/Documents/wso2/project/latency-based-kubernetes-custom-autoscaler/jmeter/jar/jtl-splitter-0.3.1-SNAPSHOT.jar

jmeter_performance_report_python_file=/home/anushiyat/Documents/wso2/project/latency-based-kubernetes-custom-autoscaler/jmeter/python/performance-report.py
jmeter_performance_report_output_file=/home/anushiyat/Documents/wso2/project/latency-based-kubernetes-custom-autoscaler/test-results/prime-10000019/auto-scaling-enabled-threshold-latency-10000-for-20min/summary.csv

actual_run_time_seconds=900
warm_up_time_minutes=5

use_case=prime
heap=100m
u=5
gc=UseParallelGC
size=10000019

total_users=$(($u))

jmeter_jtl_location=/home/anushiyat/Documents/wso2/project/latency-based-kubernetes-custom-autoscaler/test-results/prime-10000019/auto-scaling-enabled-threshold-latency-10000-for-20min/jtls
jtl_report_location=${jmeter_jtl_location}/${use_case}/${heap}_Heap_${total_users}_Users_${gc}_collector_${size}_size
jtl_file=${jtl_report_location}/results.jtl

echo $jtl_file

echo "Splitting JTL"

java -jar ${jmeter_jtl_splitter_jar_file} -f $jtl_file -t ${warm_up_time_minutes}

jtl_file_measurement_for_this=${jtl_report_location}/results-measurement.jtl


echo "Adding data to CSV file"

python3 ${jmeter_performance_report_python_file} ${jmeter_performance_report_output_file} ${jtl_file} ${actual_run_time_seconds} ${use_case} ${heap} ${u} ${gc} ${size} 
