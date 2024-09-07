#!/usr/bin/python3


import requests


def number_of_subscribers(subreddit):
	#define the URL for the subreddit API
	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

	# Define custom headers including User-Agent to avoid getting blocked
	headers = {'User-Agent': 'my-subreddit-query/0.0.1'}

	# Make the GET request to Reddit's API
	try:
		response = requests.get
		(url, headers=headers, allow_redirects=False)

		# Check if the request was successful
		if response.status_code == 200:
			data = response.json()
			return data['data']['subscribers']
		else:
			return 0
	except requests.RequestException:
		# In case of any other exceptions, return 0
		return 0
