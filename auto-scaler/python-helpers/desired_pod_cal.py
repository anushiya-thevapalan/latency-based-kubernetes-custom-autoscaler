import math

def compute_desired_pods(current_latency, desired_latency, current_pods, min_pods, max_pods):

    desired_pods = math.ceil(current_latency/desired_latency * current_pods)
    if desired_pods > max_pods:
        return max_pods
    elif desired_pods < min_pods:
        return min_pods
    else:
        return desired_pods