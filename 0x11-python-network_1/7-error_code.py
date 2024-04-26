#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    result = requests.get(url)
    if result.status_code >= 400:
        print("Error code: {}".format(result.status_code))
    else:
        print(result.text)