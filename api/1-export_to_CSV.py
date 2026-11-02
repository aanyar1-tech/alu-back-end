#!/usr/bin/python3
"""
A Python script that, using a REST API for a given employee ID,
exports all TODO list tasks in CSV format.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = int(sys.argv[1])
        
        base_url = "https://jsonplaceholder.typicode.com/"
        
        # Fetch user details
        user_response = requests.get("{}users/{}".format(base_url, employee_id))
        user_data = user_response.json()
        employee_username = user_data.get("username")
        
        # Fetch all todos for the employee
        todos_response = requests.get(
            "{}todos".format(base_url),
            params={"userId": employee_id}
        )
        todos_data = todos_response.json()
        
        # Define CSV file name
        filename = "{}.csv".format(employee_id)
        
        # Write tasks to CSV using csv.QUOTE_ALL to match required format
        with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in todos_data:
                writer.writerow([
                    employee_id,
                    employee_username,
                    task.get("completed"),
                    task.get("title")
                ])
