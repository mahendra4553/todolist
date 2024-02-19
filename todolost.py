def add_task(tasks, description):
    tasks[description] = "Pending"

def mark_task_as_done(tasks, description):
    if description in tasks:
        tasks[description] = "Done"
    else:
        print("Task not found.")

def display_tasks(tasks):
    if tasks:
        print("Tasks:")
        for task, status in tasks.items():
            print(f"{task} - {status}")
    else:
        print("No tasks in the list.")

def main():
    tasks = {}

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '2':
            description = input("Enter task description to mark as done: ")
            mark_task_as_done(tasks, description)
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()