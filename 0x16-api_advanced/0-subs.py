#!/usr/bin/python3


from  requests import get


def number_of_subscribers(subreddit):
    response = get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                   headers={'User-Agent': 'MyRedditBot/1.0 (u/Shot-Hasna-app0)'})
    # non-existent subreddits sometimes return 404
    if response.status_code != 200:
        return 0
    # and sometimes return a dummy JSON dict with only 'Listing' key
    return response.json().get('data').get('subscribers', 0)
