#!/usr/bin/python3
"""GitHub commits using the GitHub API"""

import requests
from sys import argv

if __name__ == "__main__":
    repo_name = argv[1]
    owner_name = argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    try:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    except ValueError:
        print("Not a valid JSON")
