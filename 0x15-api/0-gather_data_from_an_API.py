#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"

    urlGet = requests.get(url + "/todos")
    urlGet2 = requests.get(url)

    todos = urlGet.json()
    name = urlGet2.json()
    complete = 0
    for todo in todos:
        if todo['completed'] is True:
            complete += 1
    print(f"Employee {name['name']} is done with tasks({complete}/{len(todos)}):")
    for todo in todos:
        if todo['completed'] is True:
            print(f"\t {todo['title']}")
