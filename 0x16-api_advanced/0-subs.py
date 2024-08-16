#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    # Define the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    #set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyRedditAPI/0.0.1'}

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the status code indicates a successful response
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Return the number of subscribers
        return data.get("data", {}).get("subscribers", 0)
    else:
        # If the subreddit is invalid, return 0
        return 0
