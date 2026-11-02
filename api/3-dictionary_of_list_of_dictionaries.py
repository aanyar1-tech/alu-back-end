#!/usr/bin/python3
"""
A Python script that, using a REST API, exports all TODO list tasks
from all employees in JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch all users
    users_response = requests.get("{}users".format(base_url))
    users_data = users_response.json()

    # Fetch all todos
    todos_response = requests.get("{}todos".format(base_url))
    todos_data = todos_response.json()

    # Map user IDs to their usernames
    users_dict = {}
    for user in users_data:
        users_dict[user.get("id")] = user.get("username")

    # Build the dictionary of list of dictionaries
    all_tasks_dict = {}
    for user_id, username in users_dict.items():
        user_todos = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos_data
            if task.get("userId") == user_id
        ]
        all_tasks_dict[str(user_id)] = user_todos

    # Export to JSON file
    filename = "todo_all_employees.json"
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(all_tasks_dict, f)
