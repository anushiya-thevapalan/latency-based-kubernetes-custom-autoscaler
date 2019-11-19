log_file_creator="../python/log_files_creator.py"
metrics_server_web_app="../python/monitoring_server.py"


echo "creating all the required log files"
python3 $log_file_creator

echo "Initializing the metrics server"
python3 $metrics_server_web_app
