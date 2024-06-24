#!/usr/bin/python3
"""
This script fetches and displays employee TODO list progress from a REST API.
"""
import json
import sys
import urllib.request

def get_employee_todo_progress(employee_id):
    """
    Fetches and displays employee TODO list progress from a REST API.

    Args:
        employee_id: The ID of the employee.

    Returns:
        None
    """
    if len(sys.argv) != 2:
        print("Usage: python todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode('utf-8'))

    done_tasks = 0
    for task in data:
        if task.get('completed'):
            done_tasks += 1

    employee_name = data[0].get('userId', 'Unknown Employee')
    total_tasks = len(data)

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in data:
        if task.get('completed'):
            print(f"\t{task.get('title')}")

if __name__ == "__main__":
    get_employee_todo_progress(employee_id)
