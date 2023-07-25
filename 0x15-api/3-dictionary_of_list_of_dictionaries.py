#!/usr/bin/python3
"""
Script that uses a REST API, for a given employee ID and exports the data
in JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    num_users = len(requests.get(
                        'https://jsonplaceholder.typicode.com/users/').json())
    for num in range(1, num_users + 1):
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(num)
        username = requests.get(url).json().get('name')

        todo = requests.get(url + '/todos/')

        with open('todo_all_employees.json', 'a') as file:
            json.dump({num: [{
                "username": username,
                "task": t.get("title"),
                "completed": t.get("completed")
                } for t in todo.json()]}, file)
