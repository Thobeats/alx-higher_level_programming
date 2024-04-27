#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses
the GitHub API to display your id
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
    if result.status_code is 200:
        resultJson = result.json()
        print(resultJson['id'])
    else:
        print("None")
