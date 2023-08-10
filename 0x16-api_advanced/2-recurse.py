#!/usr/bin/python3
""" Queries the Reddit API for hot posts """
import requests


def recurse(subreddit, hot_list=[], aft=""):
    """
    Recursively queries the Reddit API and returns a list of the titles all the
    hot posts for a given subreddit
    """
    if len(aft) > 0 and aft is not None:
        base_url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={aft}'
    else:
        base_url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    response = requests.get(base_url, headers={'User-agent': 'ALX_SE'},
                            allow_redirects=False)
    if response:
        for d in response.json()['data']['children']:
            hot_list.append(d['data']['title'])

        after = response.json()['data']['after']
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)

    else:
        return None
