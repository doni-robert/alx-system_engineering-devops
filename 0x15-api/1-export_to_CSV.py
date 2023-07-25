#!/usr/bin/python3
"""
Script that uses a REST API, for a given employee ID and exports the data
in the CSV format.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    num = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(num)
    username = requests.get(url).json().get('name')

    todo = requests.get(url + '/todos/')

    with open('{}.csv'.format(num), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for t in todo.json():
            writer.writerow(
                    [num, username, t.get('completed'), t.get('title')])
