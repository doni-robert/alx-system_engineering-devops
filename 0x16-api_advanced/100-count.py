#!/usr/bin/python3
""" Queries the Reddit API for hot posts """
import requests


def count_words(subreddit, word_list, count_dict={}, aft=""):
    """
    Recursively queries the Reddit API and prints a sorted count of given
    case-insesitive keywords from hot posts for a given subreddit
    """
    if len(aft) > 0 and aft is not None:
        base_url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={aft}'
    else:
        base_url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    response = requests.get(base_url, headers={'User-agent': 'ALX_SE'},
                            allow_redirects=False)
    if response.status_code == 200:
        for d in response.json()['data']['children']:
            title = d['data']['title']
            for word in word_list:
                count = word.lower().count(title.lower())
                if word in count_dict:
                    count_dict[word] += count
                else:
                    count_dict[word] = count
        after = response.json()['data']['after']
        if after is None:
            final_dict = dict(sorted(count_dict.items(),
                                     key=lambda item: item[1],
                                     reverse=True, ))
            for key, value in final_dict.items:
                print(f'{key}: {value}')
        return count_words(subreddit, word_list, count_dict, after)
    print()
