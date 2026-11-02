#!/usr/bin/python3
"""
A Python script that, using a REST API for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]
        
        # Base URL for the REST API
        base_url = "https://jsonplaceholder.typicode.com/"
        
        # Fetch user information
        user_response = requests.get(f"{base_url}users/{employee_id}")
        user_data = user_response.json()
        employee_name = user_data.get("name")
        
        # Fetch todos for the user
        todos_response = requests.get(f"{base_url}todos", params={"userId": employee_id})
        todos_data = todos_response.json()
        
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task.get("completed")]
        number_of_done_tasks = len(done_tasks)
        
        # Display the progress summary
        print(
            f"Employee {employee_name} is done with tasks("
            f"{number_of_done_tasks}/{total_tasks}):"
        )
        
        # Display the titles of completed tasks
        for task in done_tasks:
            print(f"\t {task.get('title')}")
