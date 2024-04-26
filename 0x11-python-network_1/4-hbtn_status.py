#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
        import requests
        url = 'https://alx-intranet.hbtn.io/status'
        # Make a GET request
        result = requests.get(url)
        # resf means response format
        resf = "Body response:\n"
        resf += "\t- type: {}\n"
        resf += "\t- content: {}"
        resf = resf.format(type(result.text), result.text)
        print(resf)
