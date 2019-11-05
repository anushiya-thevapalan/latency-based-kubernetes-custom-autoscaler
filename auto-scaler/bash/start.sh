URL="https://kubernetes/apis/apps/v1/namespaces/default/deployments/ballerina-prime-testing/scale"
TOKEN=/var/run/secrets/kubernetes.io/serviceaccount/token
CA_CERT=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt

dir="$(pwd)"
python_file="$(dirname "$dir")/python-helpers/auto-scale-pods.py"

runtime="10 minute"
endtime=$(date -ud "$runtime" +%s)

while [[ $(date -u +%s) -le $endtime ]]
do
    echo "Time Now: `date +%H:%M:%S`"

    echo "Getting latency details"
    latency_response=$(curl 10.32.2.22:8000)

    curl --cacert ${CA_CERT} -H 'Accept: application/json' -H "Authorization: Bearer $(cat ${TOKEN})" ${URL} > scale.json

    echo "Updating the scale.json file with required number of pods"
    python3 $python_file $latency_response
    
    echo "scaling"
    curl -X PUT -d@scale.json --cacert ${CA_CERT} -H 'Content-Type: application/json' -H "Authorization: Bearer $(cat ${TOKEN})" $URL

    echo "Sleeping for 60 seconds"
    sleep 60
done