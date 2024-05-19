#!/usr/bin/python3
import urllib.request

all_attributes_methods = dir(urllib.request.urlopen)

methods = [attr for attr in all_attributes_methods if callable(getattr(urllib.request.urlopen, attr))]
attributes = [attr for attr in all_attributes_methods if not callable(getattr(urllib.request.urlopen, attr))]

print("Methods:")
for method in methods:
    print(method)
print("\nAttributes:")
for attribute in attributes:
    print(attribute)