def view_tasks():
    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def main():
    print("Welcome to Smart Task Manager")
    add_task("Sample Task")
    view_tasks()