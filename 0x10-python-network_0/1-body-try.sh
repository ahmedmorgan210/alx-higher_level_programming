#!/bin/bash
# desplay the reponse in case of state 200
curl -sL $1 | { read -r status; echo "$status"; if [ "$status" = "HTTP/1.1 200 OK" ]; then cat; fi; }
