#!/bin/bash

URL="https://kubernetes/api/v1/namespaces/default/endpoints/ballerina-prime-testing-svc"
TOKEN=/var/run/secrets/kubernetes.io/serviceaccount/token
CA_CERT=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt

echo "Time Now: `date +%H:%M:%S`"
curl --cacert ${CA_CERT} -H 'Accept: application/json' -H "Authorization: Bearer $(cat ${TOKEN})" ${URL} > endpoints.json
    
