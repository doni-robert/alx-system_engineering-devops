#!/usr/bin/python3
"""
Script that uses a REST API, for a given employee ID and exports the data
in JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    with open('todo_all_employees.json', 'w') as file:
        users = requests.get(
                    'https://jsonplaceholder.typicode.com/users').json()
        todo = requests.get(
                    'https://jsonplaceholder.typicode.com/todos/').json()
        json.dump({user.get("id"): [{
            "username": user.get("username"),
            "task": t.get("title"),
            "completed": t.get("completed")
            } for t in todo if user.get("id") == t.get("userId")]
            for user in users}, file)
