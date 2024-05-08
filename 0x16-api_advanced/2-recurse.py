#!/usr/bin/python3
"""
1-top_ten
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    global after
    headers = {'User-Agent': 'MyAPI/0.0.4'}
    parameters = {'after': after}
    response = requests.get(url, params=parameters,
                            headers=headers, allow_redirects=False)
    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        data = response.json()['data']['children']
        for child in data:
            hot_list.append(child['data']['title'])
        return hot_list
    return None
