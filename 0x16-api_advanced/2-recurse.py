#!/usr/bin/python3


import requests


def recurse(subreddit, hot_list=[], after=None):
    # Reddit API endpoint for hot posts
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    
    # Custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'MyBot/0.0.1'
    }
    
    # Parameters for the API request
    params = {'limit': 100}
    if after:
        params['after'] = after
    
    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the request was successful and the subreddit exists
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            # Add titles of current page to hot_list
            for post in posts:
                hot_list.append(post['data']['title'])
            
            # Check if there are more pages
            after = data['data']['after']
            if after:
                # Recursive call with the new 'after' value
                return recurse(subreddit, hot_list, after)
            else:
                # No more pages, return the complete list
                return hot_list
        elif response.status_code == 404:
            # Subreddit not found
            return None
        else:
            # Other error occurred
            return None
    except:
        # If there's any exception (e.g., connection error), return None
        return None

# Wrapper function to match the required prototype
def recurse_wrapper(subreddit, hot_list=[]):
    return recurse(subreddit)
