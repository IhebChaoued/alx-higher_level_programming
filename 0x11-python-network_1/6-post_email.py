#!/usr/bin/python3
"""Post request"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}

    response = requests.post(url, data)
    print(response.text)
