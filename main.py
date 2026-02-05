tasks = []


def show_menu():
    print("\nSmart Task Manager")
    print("------------------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


def add_task():
    task = input("Enter task description: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task():
    view_tasks()
    try:
        choice = int(input("Enter task number to delete: "))
        removed_task = tasks.pop(choice - 1)
        print(f"Task '{removed_task}' deleted.")
    except (ValueError, IndexError):
        print("Invalid task number.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting Smart Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()