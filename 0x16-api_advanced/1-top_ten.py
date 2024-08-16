#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and
print the titles of the first 10 hot posts for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles f the first 10 hot posts
    for the given subreddit.
    If the subreddit is invalid, print None.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'MyRedditAPI/0.0.1'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params,
allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            if not posts:
                print(None)
            else:
                for post in posts:
                    print(post.get("data", {}).get("title"))
        else:
            print(None)
    except requests.RequestException:
        print(None)
