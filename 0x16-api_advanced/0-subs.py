#!/usr/bin/python3


import requests


def number_of_subscribers(subreddit):
    # Use .format() for string formatting,
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'my-subreddit-query/0.0.1'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
