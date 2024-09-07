#!/usr/bin/python3


from requests import get


def number_of_subscribers(subreddit):
<<<<<<< HEAD
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
=======
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
>>>>>>> dfd54ec0444b6d2117a930561f68963f56bb04e8
