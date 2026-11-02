#!/usr/bin/python3
"""
A Python script that, using a REST API for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = int(sys.argv[1])
        base_url = "https://jsonplaceholder.typicode.com/"

        user_url = "{}users/{}".format(base_url, emp_id)
        user_response = requests.get(user_url)
        user_data = user_response.json()
        emp_name = user_data.get("name")

        todos_url = "{}todos".format(base_url)
        todos_response = requests.get(
            todos_url,
            params={"userId": emp_id}
        )
        todos_data = todos_response.json()

        total_tasks = len(todos_data)
        done_tasks = [t for t in todos_data if t.get("completed")]
        num_done = len(done_tasks)

        print(
            "Employee {} is done with tasks({}/{}):".format(
                emp_name, num_done, total_tasks
            )
        )

        for task in done_tasks:
            print("\t {}".format(task.get("title")))
