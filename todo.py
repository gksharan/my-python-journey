def add_task():
    task = input("Enter your task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

def delete_task():
    view_tasks()
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    task_num = int(input("Enter task number to delete: "))
    if 1 <= task_num <= len(tasks):
        del tasks[task_num - 1]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task deleted!")
    else:
        print("Invalid number!")

def todo():
    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

todo()
