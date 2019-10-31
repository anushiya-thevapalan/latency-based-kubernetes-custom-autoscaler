pod_count=${1}
file_to_be_modified="$(pwd)/scale.json"
python_file="$(dirname "$dir")/python-helper/modify-json-with-replica-count.py"
API_URL="http://localhost:8080/apis/extensions/v1beta1/namespaces/default/deployments/ballerina-prime-testing/scale"

curl  -H 'Accept: application/json' $API_URL > scale.json
#jq --arg pod $pod_count '.spec.replicas = $pod' scale.json > scale1.json && mv scale1.json scale.json

#cat scale.json | jq --arg pod $pod_count '.spec.replicas = $pod' > scale1.json && mv scale1.json scale.json

#cat scale.json | jq '.spec.replicas = 1' > scale1.json && mv scale1.json scale.json

python3 



curl -X PUT -d@scale.json -H 'Content-Type: application/json' $API_URL
