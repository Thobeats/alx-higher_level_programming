#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import urllib.request as urlreq
    import urllib.parse as urlparse
    import sys
    url = sys.argv[1]
    data = {
        "email": sys.argv[2]
    }
    data = urlparse.urlencode(data).encode('utf8')
    # Make a GET request
    with urlreq.urlopen(url, data) as response:
        result = response.read()
        print(result.decode())
