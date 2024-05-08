#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.4'}
    params = {"limit": 10}
    response = requests.get(url, params=params,
                            headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']['children']
        for child in data:
            print(child['data']['title'])
        return
    print(None)
