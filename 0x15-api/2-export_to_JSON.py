#!/usr/bin/python3
"""
Script that uses a REST API, for a given employee ID and exports the data
in JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    num = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(num)
    username = requests.get(url).json().get('username')

    todo = requests.get(url + '/todos/')

    with open('{}.json'.format(num), 'w') as file:
        json.dump({num: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
            } for t in todo.json()]}, file)
