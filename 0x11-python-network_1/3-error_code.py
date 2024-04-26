#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import urllib.request as urlreq
    import urllib.parse as urlparse
    from urllib.error import HTTPError
    import sys
    url = sys.argv[1]
    try:
        # Make a GET request
        with urlreq.urlopen(url) as response:
            result = response.read()
            print(result.decode())
    except HTTPError as e:
        print("Error code: {}".format(e.code))
