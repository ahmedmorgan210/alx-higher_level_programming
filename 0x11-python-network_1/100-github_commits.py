#!/usr/bin/python3
"""Python script to fetch and print the 10 most\
      recent commits from a GitHub repository"""

import requests
import sys

# The base URL for the GitHub API
base_url = "https://api.github.com/repos"

# The repository and owner names are passed as command-line arguments
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# Construct the URL for the API request
url = f"{base_url}/{owner_name}/{repo_name}/commits"

# Send a GET request to the GitHub API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    commits = response.json()
    # Print the 10 most recent commits
    for commit in commits[:10]:
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")
else:
    print(f"Error: Unable to fetch commits. \
          Status code: {response.status_code}")
