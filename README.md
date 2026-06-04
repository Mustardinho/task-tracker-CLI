# Task Tracker CLI

A lightweight, purely native command-line interface (CLI) application to track and manage your tasks. This project is built entirely with Python's standard library, requiring absolutely no external frameworks or dependencies.

## 🚀 Features

* **Create** new tasks with a description.
* **Update** the description of existing tasks.
* **Delete** tasks you no longer need.
* **Update Status:** Mark tasks as `in-progress` or `done`.
* **View Tasks:** List all tasks, or filter them by their current status (`todo`, `in-progress`, `done`).
* **Persistent Storage:** Tasks are automatically saved to a local `tasks.json` file, creating the file automatically on the first run.

## 🛠️ Prerequisites

* Python 3.x installed on your system.

## 💻 Usage

Open your terminal and navigate to the directory containing `task-cli.py`. You can run the application by typing `python task-cli.py` followed by a command.

### 1. Adding a Task
Creates a new task with a default status of `todo`. If your description has spaces, wrap it in quotation marks.
```bash

Project URL: https://roadmap.sh/projects/task-tracker
