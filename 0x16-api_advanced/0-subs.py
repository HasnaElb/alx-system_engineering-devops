#!/usr/bin/python3
"""
This module provides a function to query the Reddit API
and return the number of subscribers for a given subreddit.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Query Reddit API and return the number of subscribers for a given
    subreddit.
    If the subreddit is invalid, return 0.
    """
    response = get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                   headers={'User-Agent': 'Mozilla/5.0'})
    # non-existent subreddits sometimes return 404
    if response.status_code != 200:
        return 0
    # and sometimes return a dummy JSON dict with only 'Listing' key
    return response.json().get('data').get('subscribers', 0)
