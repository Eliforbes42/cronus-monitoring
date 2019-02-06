#!/bin/bash

grafanaIP="http://$(sudo kubectl get svc --namespace kube-system dash-grafana -o json | jq -r .spec.clusterIP)/login"

echo "Grafana is at $grafanaIP"
