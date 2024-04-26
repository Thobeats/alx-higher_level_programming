#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request as urlreq


url = 'https://alx-intranet.hbtn.io/status'

# Make a GET request
with urlreq.urlopen(url) as response:
    result = response.read()
    # resf means response format
    resf = "Body response:\n"
    resf += "    - type: {}\n"
    resf += "    - content: {}\n"
    resf += "    - utf8 content: {}"
    resf = resf.format(type(result), result, result.decode())
    print(resf)
