#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable
found in the header of the response.
"""
import urllib.request as urlreq
import sys


url = sys.argv[1]
# Make a GET request
with urlreq.urlopen(url) as response:
    result = response.info()
    print(result['X-Request-Id'])
