#!/bin/bash
# displays the size of the body of the response
curl -sw "%{size_download}\n" $1
