import sys
import os
import json
from datetime import datetime
from pathlib import Path

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        Path("tasks.json").touch()
        print("JSON succsesfully created")
        return []
    
    with open(FILE_NAME, 'r') as f:
        try:
            tasks = json.load(f)
            return tasks
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(desc):
    tasks = load_tasks()

    if len(tasks) < 1:
        new_id = 1
    else:
        new_id = tasks[-1]['id'] + 1
    
    now = datetime.now().isoformat()

    new_task = {
        "id": new_id,
        "description": desc,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"New task added successfully (ID: {new_id})")

def list_tasks():
    tasks = load_tasks()
    if len(tasks) == 0:
        print("No tasks found")
        return
    
    for task in tasks:
        print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']} | Created at: {task['createdAt']} | Updated at: {task['updatedAt']}")

def update_task(task_id, new_description):
    tasks = load_tasks()

    task_found = False

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()

            task_found = True

            break
    
    if task_found:
        save_tasks(tasks)
        print(f"Task {task_id} updated successfully")
    else:
        print(f"Error: Task with the ID {task_id} not found")

def delete_task(task_id):
    tasks = load_tasks()
    if len(tasks) == 0:
        print("No tasks found")
        return

    tasks_to_keep = []
    task_found = False

    for task in tasks:
        if task["id"] != task_id:
            tasks_to_keep.append(task)
        else:
            task_found = True
    
    if task_found:
        save_tasks(tasks_to_keep)
        print(f"Task {task_id} deleted successfully")
    else:
        print(f"Error: Task with the ID {task_id} not found")

def mark_in_progress(task_id):
    tasks = load_tasks()
    if len(tasks) == 0:
        print("No tasks found")
        return

    task_found = False

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "In progress"
            task_found = True
            break
    
    if task_found:
        save_tasks(tasks)
        print(f"The status of the task with ID {task_id} has been changed to 'In progress'")
    else:
        print(f"Task with ID {task_id} not found")

def mark_done(task_id):
    tasks = load_tasks()
    if len(tasks) == 0:
        print("No tasks found")
        return

    task_found = False

    for task in tasks:
        if task["id"] == task_id:
            task['status'] = 'Done'

            task_found = True
            break;
    
    if task_found:
        save_tasks(tasks)
        print(f"The status of the task with ID {task_id} has been changed to 'Done'")
    else:
        print(f"Error: Task with ID {task_id} not found")

def list_progress_tasks():
    tasks = load_tasks()
    if len(tasks) == 0:
        print("No tasks found")
        return

    for task in tasks:
        if task["status"] == "In progress":
            print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']} | Created at: {task['createdAt']} | Updated at: {task['updatedAt']}")

def list_done_tasks():
    tasks = load_tasks()
    if len(tasks) == 0:
        print("No tasks found")
        return

    for task in tasks:
        if task["status"] == "Done":
            print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']} | Created at: {task['createdAt']} | Updated at: {task['updatedAt']}")

def list_todo_tasks():
    tasks = load_tasks()
    if len(sys.argv) == 0:
        print("No tasks found")
        return

    for task in tasks:
        if task["status"] == "todo":
            print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']} | Created at: {task['createdAt']} | Updated at: {task['updatedAt']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli.py <command> [arguments]")
        return
    
    command = sys.argv[1]

    if command == "add":
        description = sys.argv[2]
        add_task(description)

    elif command == "update":
        if len(sys.argv) < 3:
            print("How to update a task: task-cli.py update [taskID] [new_description]")
        elif len(sys.argv) < 4:
            print("How to update a task: task-cli.py update [taskID] [new_description]")
        else:
            task_id = int(sys.argv[2])
            new_description = sys.argv[3]
            update_task(task_id, new_description)

    elif command == "delete":
        task_id = int(sys.argv[2])
        delete_task(task_id)

    elif command == "mark-in-progress":
        task_id = int(sys.argv[2])
        mark_in_progress(task_id)
    
    elif command == "mark-done":
        task_id = int(sys.argv[2])
        mark_done(task_id)
    
    elif command == "list":
        if len(sys.argv) == 3:
            status = sys.argv[2]

            if status == "in-progress":
                list_progress_tasks()
            elif status == "done":
                list_done_tasks()
            elif status == "todo":
                list_todo_tasks()
        elif len(sys.argv)  == 2:
            list_tasks()

if __name__ == "__main__":
    main()