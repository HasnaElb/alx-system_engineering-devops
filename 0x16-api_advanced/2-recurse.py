#!/usr/bin/python3
<<<<<<< HEAD


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
=======
""" 0x16. API advanced, task 2. Recurse it!
"""
from requests import get


def recurse(subreddit, hot_list=[]):
    """ Recursively queries Reddit API, one page per frame, to compile list of
    all "hot" posts for a given subreddit.

    Args:
        subreddit (str): subreddit to query
        hot_list (list): list of dictionaries representing posts in "hot",
            compiled from lower frames in the stack

    Return:
        `hot_list` with the current API page/recursion frame's list appended
    """
    limit = 100
    after = hot_list[-1].get('data').get('name', '') if len(hot_list) else ''
    # adding request parameter `raw_json` deactivates default ampersand escape
    url = 'https://www.reddit.com/dev/api//r/{}/hot.json?raw_json=1&after={}'
    response = get(url.format(subreddit, after, limit),
                   headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code != 200:
        return None
    current_page_list = response.json().get('data').get('children', [])
    if len(current_page_list) < limit:
        return hot_list + current_page_list
    return recurse(subreddit, hot_list + current_page_list)
>>>>>>> dfd54ec0444b6d2117a930561f68963f56bb04e8
