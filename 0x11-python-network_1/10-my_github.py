#!/usr/bin/python3
"""Github API"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    response = requests.get(url, auth=auth)
    data = response.json()
    
    print(data.get("id"))
