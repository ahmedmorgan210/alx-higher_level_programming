#!/usr/bin/python3
"""display the value of the X-Request-Id variable found in the header """
from urllib.request import urlopen


with urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.getheader('X-Request-Id')

print(html)
