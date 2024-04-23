#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
returns information about his/her TOdO list progress."""
import csv
import requests
import sys


if __name__ == '__main__':
    todo = requests.get(f'https://jsonplaceholder.typicode.com/users/\
{sys.argv[1]}/todos')
    users = requests.get(f'https://jsonplaceholder.typicode.com/users/\
{sys.argv[1]}')

    todoo = todo.json()
    user = users.json()

    p = f"{sys.argv[1]}.csv"
    with open(p, "w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for i in todoo:
            writer.writerow([sys.argv[1],
                             user['username'], i['completed'], i['title']])
