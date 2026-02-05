tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully")

def main():
    print("Welcome to Smart Task Manager")
    add_task("Sample Task")  # Test
    print("Current Tasks:", tasks)

if __name__ == "__main__":
    main()