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
    params = {
        "per_page": 10,
        "page": 1,
    }
    result = requests.request('GET', url, params=params, headers=headers)
    if result.status_code == 200:
        resultJson = result.json()
        sR = sorted(resultJson,
                    key=lambda res: res['commit']['author']['date'],
                    reverse=True)
        for key, value in enumerate(sR):
            print("{}: {}".format(sR[key]['sha'],
                                  sR[key]['commit']['author']['name']))
    else:
        print("")
