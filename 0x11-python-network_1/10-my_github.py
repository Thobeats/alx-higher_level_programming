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
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    result = requests.request('GET', url,
                              headers=headers,
                              auth=requests.auth.HTTPBasicAuth(username,
                                                               password))
    print(result.json())
