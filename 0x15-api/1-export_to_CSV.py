#!/usr/bin/python3
""" Exports to-do list for employee ID to CSV format. """
import csv
import requests
import sys


if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"

    urlGet = requests.get(url + "/todos")
    urlGet2 = requests.get(url)

    todos = urlGet.json()
    name = urlGet2.json()
    file = f"{sys.argv[1] + ".csv"}"
    with open(file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            p = (sys.argv[1], name['name'], todo['completed'], todo['title'])
            csv_writer.writerow(p)
