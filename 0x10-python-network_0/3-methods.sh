#!/bin/bash
# display all available methods
curl -sIX "OPTIONS" $1 | grep -i "Allow" | awk '{for(i=2; i<=NF; i++) printf "%s%s", $i, (i==NF) ? "\n" : OFS}'
