#!/usr/bin/python3
"""Error"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(f"{response.text}")
