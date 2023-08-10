#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ Queries the Reddit API and returns the number of subscribers """
    base_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(base_url, headers={'User-agent': 'ALX_SE'},
                            allow_redirects=False)
    if response:
        subscribers = response.json().get('data').get('subscribers')
        return subscribers
    else:
        return 0
