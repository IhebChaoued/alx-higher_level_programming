#!/usr/bin/python3
"""URL and Email"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode("ascii")

    with urllib.request.urlopen(url, data) as res:
        print(res.read().decode("utf-8"))
