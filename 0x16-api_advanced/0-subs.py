#!/usr/bin/python3


import requests

def number_of_subscribers(subreddit):
    # Use .format() for string formatting, since f-strings are not supported in Python 3.4
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    headers = {
        'User-Agent': 'my-subreddit-query/0.0.1'  # Custom User-Agent to avoid 429 error
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
