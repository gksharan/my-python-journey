tasks = []

while True:
    print("\n1. view tasks")
    print("2. add task")
    print("3. delete task")
    print("4. Mark complete")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        if not tasks:
            print("No tasks found.")
        else:
            for i , task in enumerate(tasks, 1):
                print( i,task)

    if choice == "2":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added!")

    if choice == "3":
        task = int(input("enter no of task to delete: "))
        del tasks[task-1]
        print("Taske deleted!:")

    if choice =="4":
        task = int(input("enter no of task to mark complete: "))
        tasks[task-1] = tasks[task-1] + " - completed"
        print("Task marked as complete!")



    if choice == "5":
        break