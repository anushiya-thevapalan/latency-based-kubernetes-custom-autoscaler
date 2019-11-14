import subprocess

pod_count = 2
subprocess.run(['../bash/get_and_update_pods.sh', str(pod_count)])