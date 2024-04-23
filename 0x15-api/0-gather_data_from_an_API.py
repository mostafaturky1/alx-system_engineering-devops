#!/usr/bin/python3
""" module """
import requests
import sys


urlGet = requests.get
(f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos")
urlGet2 = requests.get
(f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}")

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
