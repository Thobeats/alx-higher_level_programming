#!/usr/bin/python3
"""
Python script that takes in a URL,
returns the value of the X-Request-Id variable
"""
if __name__ == "__main__":
    import urllib.request as urlreq
    import sys
    url = sys.argv[1]
    # Make a GET request
    with urlreq.urlopen(url) as response:
        result = response.info()
        header = result.get('X-Request-Id')
        print(header)
