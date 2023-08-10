#!/usr/bin/python3
""" Queries the Reddit API for hot posts """
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit
    """
    base_url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(base_url, headers={'User-agent': 'ALX_SE'},
                            allow_redirects=False)
    if response:
        for d in response.json()['data']['children']:
            print(d['data']['title'])
    else:
        print('None')
