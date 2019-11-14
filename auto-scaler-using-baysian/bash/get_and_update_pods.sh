#!/bin/sh

number_of_pods=$1

URL="https://kubernetes/apis/apps/v1/namespaces/default/deployments/ballerina-prime-testing/scale"
TOKEN=/var/run/secrets/kubernetes.io/serviceaccount/token
CA_CERT=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt

dir="$(pwd)"
python_file="$(dirname "$dir")/python/modify_json_with_replica_count.py"


echo "Time Now: `date +%H:%M:%S`"

curl --cacert ${CA_CERT} -H 'Accept: application/json' -H "Authorization: Bearer $(cat ${TOKEN})" ${URL} > scale.json

echo "Updating the scale.json file with required number of pods"
python3 $python_file $number_of_pods

echo "scaling"
curl -X PUT -d@scale.json --cacert ${CA_CERT} -H 'Content-Type: application/json' -H "Authorization: Bearer $(cat ${TOKEN})" $URL

