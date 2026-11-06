#!/usr/bin/python3
"""
Python script that returns information about an employee's TODO list progress
using a REST API given an employee ID as a parameter.
"""

import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        
        user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
        
        user_res = requests.get(user_url)
        todos_res = requests.get(todos_url)
        
        if user_res.status_code == 200 and todos_res.status_code == 200:
            user_data = user_res.json()
            todos_data = todos_res.json()
            
            emp_name = user_data.get('name')
            total_tasks = len(todos_data)
            
            done_tasks = [task for task in todos_data if task.get('completed') is True]
            num_done = len(done_tasks)
            
            print(f"Employee {emp_name} is done with tasks({num_done}/{total_tasks}):")
            
            for task in done_tasks:
                print(f"\t {task.get('title')}")
