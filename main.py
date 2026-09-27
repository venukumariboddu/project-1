def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def add_task(tasks):
    task = input("\nEnter a new task: ")

    if task.strip():
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def delete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()