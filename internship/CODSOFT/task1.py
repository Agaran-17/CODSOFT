python /c:/internship/CODSOFT/task1.py
import os

# File to store tasks
TODO_FILE = "todo.txt"

def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_menu():
    """Display the menu options."""
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")

def mark_completed(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num] = f"[Completed] {tasks[task_num]}"
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the To-Do List application."""
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()