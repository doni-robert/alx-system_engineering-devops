#!/usr/bin/python3
"""
Script that uses a REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    num = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(num)
    username = requests.get(url).json().get('name')

    todo = requests.get(url + '/todos/')

    complete = total = 0
    done_list = []
    for data in todo.json():
        if data.get('completed') is True:
            complete += 1
            done_list.append(data.get('title'))
        else:
            total += 1

    total += complete

    print("Employee {} is done with tasks({}/{}):".format(
                                                    username, complete, total))
    for data in done_list:
        print("\t {}".format(data))
