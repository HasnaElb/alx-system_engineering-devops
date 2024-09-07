#!/usr/bin/python3


from requests import get


def number_of_subscribers(subreddit):
	# Use .format() for string formatting,
	response = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
		headers={'User-Agent': 'MyBot/0.0.1'})

	if response.status_code != 200:
		return 0
	return response.json().get('data').get('subscribers', 0)
