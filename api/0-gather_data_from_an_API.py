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
        
        base_url = "https://jsonplaceholder.typicode.com/"
        
        user_response = requests.get(f"{base_url}users/{employee_id}")
        user_data = user_response.json()
        employee_name = user_data.get("name")
        
        todos_response = requests.get(
            f"{base_url}todos",
            params={"userId": employee_id}
        )
        todos_data = todos_response.json()
        
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task.get("completed")]
        number_of_done_tasks = len(done_tasks)
        
        print(
            f"Employee {employee_name} is done with tasks("
            f"{number_of_done_tasks}/{total_tasks}):"
        )
        
        for task in done_tasks:
            print(f"\t {task.get('title')}")
