tasks = []

def add_task():
    task_name = input("Enter task name: ")
    tasks.append({"name": task_name, "done": False})
    print("Task added.")

def list_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not done"
        print(f"{i}. {task['name']} - {status}")

def mark_task_done():
    list_tasks()
    task_num = int(input("Enter the task number to mark as done: ")) - 1

    if 0 <= task_num < len(tasks):
        tasks[task_num]["done"] = True
        print("Task marked as done.")
    else:
        print("Invalid task number.")

def remove_task():
    list_tasks()
    task_num = int(input("Enter the task number to remove: ")) - 1

    if 0 <= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f"Task '{removed_task['name']}' removed.")
    else:
        print("Invalid task number.")

while True:
    print("\nTo-Do List Application")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please select a valid option.")

print("Goodbye!")
