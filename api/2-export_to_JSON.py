#!/usr/bin/python3
"""
A Python script that, using a REST API for a given employee ID,
exports all TODO list tasks in JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = int(sys.argv[1])
        base_url = "https://jsonplaceholder.typicode.com/"

        # Fetch user details
        user_url = "{}users/{}".format(base_url, emp_id)
        user_response = requests.get(user_url)
        user_data = user_response.json()
        emp_username = user_data.get("username")

        # Fetch all todos for the employee
        todos_url = "{}todos".format(base_url)
        todos_response = requests.get(
            todos_url,
            params={"userId": emp_id}
        )
        todos_data = todos_response.json()

        # Build the list of task dictionaries matching required keys
        tasks_list = []
        for task in todos_data:
            tasks_list.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": emp_username
            })

        # Construct the final dictionary structure { "USER_ID": [...] }
        # Note: The keys in JSON output should be strings (e.g., "2")
        out_data = {
            str(emp_id): tasks_list
        }

        # Define JSON filename
        filename = "{}.json".format(emp_id)

        # Write to JSON file
        with open(filename, mode="w", encoding="utf-8") as f:
            json.dump(out_data, f)
