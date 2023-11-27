#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


import requests
import sys

def get_employee_todo_progress(employee_id):
    # API endpoint for todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # API endpoint for user details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    try:
        # Fetching user details
        user_response = requests.get(user_url)
        user_data = user_response.json()

        # Fetching todos for the given employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Extracting relevant information
        employee_name = user_data.get('name')
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task['completed']]
        number_of_done_tasks = len(completed_tasks)

        # Displaying information
        print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_tasks}):")
        print(f"{employee_name}: {number_of_done_tasks}/{total_tasks}")

        # Displaying completed tasks
        if completed_tasks:
            print("Completed tasks:")
            for task in completed_tasks:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
