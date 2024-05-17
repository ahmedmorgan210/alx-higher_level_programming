#!/usr/bin/python3
"""display the value of the X-Request-Id variable found in the header """
from urllib.request import urlopen
import sys


with urlopen(sys.argv[1]) as response:
    html = response.getheader('X-Request-Id')

print(html)
