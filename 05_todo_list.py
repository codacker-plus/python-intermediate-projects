# todo_list.py
def load_tasks():
    """Load tasks from a file."""
    try:
        with open('tasks.txt', 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to a file."""
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def todo_list():
    """Main function for to-do list."""
    tasks = load_tasks()
    print("To-Do List")

    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")
        elif choice == '2':
            if not tasks:
                print("No tasks to remove!")
                continue
            print("Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                save_tasks(tasks)
                print("Task removed!")
            else:
                print("Invalid task number!")
        elif choice == '3':
            if not tasks:
                print("No tasks!")
            else:
                print("Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    todo_list()
