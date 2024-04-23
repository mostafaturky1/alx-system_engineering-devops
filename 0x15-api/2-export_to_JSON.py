#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
returns information about his/her TOdO list progress."""
import json
import requests
import sys


if __name__ == '__main__':
    todo = requests.get(f'https://jsonplaceholder.typicode.com/users/\
{sys.argv[1]}/todos')
    users = requests.get(f'https://jsonplaceholder.typicode.com/users/\
{sys.argv[1]}')

    todoo = todo.json()
    user = users.json()

    p = f"{sys.argv[1]}.json"
    with open(p, "w") as file:
        newDict = []
        for i in todoo:
            newDict.append({"task": i['title'], "completed": i['completed'],
                            "username": user['username']})
        json.dump({sys.argv[1]: newDict}, file)
