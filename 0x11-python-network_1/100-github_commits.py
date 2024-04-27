#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
Print all commits by: `<sha>: <author name>` (one by line)
"""
if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    result = requests.request('GET', url, headers=headers)
    if result.status_code == 200:
        resultJson = result.json()
        i = 0
        while i < 10:
            print("{}: {}".format(resultJson[i]['sha'],
                                  resultJson[i]['commit']['author']['name']))
            i = i + 1
