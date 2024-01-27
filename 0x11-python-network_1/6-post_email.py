#!/usr/bin/python3
"""Post request"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print("Your email is: {}".format(response.text))
