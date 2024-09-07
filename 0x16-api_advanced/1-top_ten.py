#!/usr/bin/python3
""" 0x16. API advanced, task 1. Top Ten
"""


from requests import get


def top_ten(subreddit):
    """ Queries Reddit API and prints titles of first 10 "hot" posts listed for
    a given subreddit.

    Args:
        subreddit (str): subreddit to query
    """
    # adding request parameter `raw_json` deactivates default ampersand escape
    url = 'https://www.reddit.com/r/{}/hot.json?raw_json=1'
    response = get(url.format(subreddit),
<<<<<<< HEAD
                   headers={'User-Agent': 'Hasna'})
=======
                   headers={'User-Agent': 'Mozilla/5.0'})
>>>>>>> dfd54ec0444b6d2117a930561f68963f56bb04e8
    if response.status_code != 200:
        print(None)
        return
    hot_posts = response.json().get('data').get('children', [])
    if not hot_posts:
        print(None)
        return
    for i, post in enumerate(hot_posts):
        if i == 10:
            break
        print(post.get('data').get('title', ''))
