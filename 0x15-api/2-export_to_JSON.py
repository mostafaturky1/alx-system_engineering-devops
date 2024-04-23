#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID
returns information about his/her TOdO list progress."""
import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]

    response_user = requests.get(f"https://jsonplaceholder.typicode.com/\
users/{user_id}")
    user = response_user.json()

    response_todos = requests.get(f"https://jsonplaceholder.typicode.com/\
todos?userId={user_id}")
    todos = response_todos.json()

    todos_list = []

    for todo in todos:
        todos_list.append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": user['username']
        })

    with open(f"{user_id}.json", 'w') as json_file:
        json.dump({user_id: todos_list}, json_file)
