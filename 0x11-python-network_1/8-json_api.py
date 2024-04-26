#!/usr/bin/python3
"""
Write a Python script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    data = {}
    if (len(sys.argv) < 2):
        data['q'] = ""
    else:
        data['q'] = sys.argv[1]
    try:
        result = requests.post(url, data)
        result.raise_for_status()
    except requests.exceptions.InvalidJSONError:
        print("Not a valid JSON")
    else:
        res = result.json()
        if (len(res) == 0):
            print("No content")
        else:
            print("[{}] {}".format(res['id'], res['name']))
