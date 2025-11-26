tasks = []

def show_menu():
    print("\n----- TO-DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            print("\nSelect a task number to remove:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            num = int(input("Task number: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again.")