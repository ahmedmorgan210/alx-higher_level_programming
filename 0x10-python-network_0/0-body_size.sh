#!/bin/bash
# displays the size of the body of the response
curl -sIG "$1" | awk '/Content-Length/ {print $2}
