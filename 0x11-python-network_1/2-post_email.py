#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
import sys
import urllib
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode("utf-8")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        the_response_bytes = response.read()

    the_response_str = the_response_bytes.decode('utf-8')
    print(the_response_str)
