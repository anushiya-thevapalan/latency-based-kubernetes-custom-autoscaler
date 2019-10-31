
URL="https://kubernetes/api/v1/namespaces/default/endpoints/ballerina-prime-testing-svc"
TOKEN=/var/run/secrets/kubernetes.io/serviceaccount/token
CA_CERT=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt

python_web_app="../python/web_app.py"

runtime="10 minute"
endtime=$(date -ud "$runtime" +%s)

while [[ $(date -u +%s) -le $endtime ]]
do
    echo "Time Now: `date +%H:%M:%S`"
    curl --cacert ${CA_CERT} -H 'Accept: application/json' -H "Authorization: Bearer $(cat ${TOKEN})" ${URL} > endpoints.json

    echo "Pull metrics"
    python3 $python_web_app
    
    echo "Sleeping for 60 seconds"
    sleep 60
done