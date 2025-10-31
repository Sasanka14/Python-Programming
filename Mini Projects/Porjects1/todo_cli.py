"""
🎯 Project Title: Command-Line Mini Project — Advanced To-Do Manager
File: todo_cli_advanced.py

📘 Objective:
Build a persistent text-based To-Do List app that allows:
- Adding tasks
- Viewing all tasks
- Completing tasks
- Auto-saving data to JSON file

This project enhances the basic version by introducing:
- File handling (JSON)
- Task timestamps
- Status tracking (Pending/Completed)
- Data persistence between sessions
"""

import json
from datetime import datetime
from pathlib import Path

# -------------------------------
# Constants
# -------------------------------
FILE_PATH = Path("tasks.json")

# -------------------------------
# Load existing tasks
# -------------------------------
def load_tasks():
    if FILE_PATH.exists():
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    return []


# -------------------------------
# Save tasks to file
# -------------------------------
def save_tasks(tasks):
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=4)


# -------------------------------
# Display tasks
# -------------------------------
def list_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks yet.")
        return
    print("\n📝 Your To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✅ Done" if task["completed"] else "🕒 Pending"
        print(f"{i}. {task['title']}  [{status}] (added: {task['added']})")


# -------------------------------
# Add new task
# -------------------------------
def add_task(tasks):
    title = input("Enter task name: ").strip()
    if not title:
        print("⚠️ Task name cannot be empty.")
        return
    task = {
        "title": title,
        "completed": False,
        "added": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'✅ Task "{title}" added successfully!')


# -------------------------------
# Complete task
# -------------------------------
def complete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("\nEnter task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            save_tasks(tasks)
            print(f'🎉 Marked "{tasks[num - 1]["title"]}" as completed!')
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


# -------------------------------
# Main Loop
# -------------------------------
def main():
    tasks = load_tasks()
    while True:
        print("\n===========================")
        print("📋  To-Do List Manager")
        print("===========================")
        print("1️⃣  Add Task")
        print("2️⃣  List Tasks")
        print("3️⃣  Complete Task")
        print("4️⃣  Quit")
        print("===========================")

        choice = input("Choose an option (1–4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("\n👋 Bye! Your tasks are saved automatically.")
            break
        else:
            print("⚠️ Invalid option. Try again.")


# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    main()
