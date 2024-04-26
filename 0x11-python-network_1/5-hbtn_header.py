#!/usr/bin/python3
"""
Python script that takes in a URL,
returns the value of the X-Request-Id variable
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    # Make a GET request
    result = requests.get(url)
    header = result.headers.get('X-Request-Id')
    print(header)
