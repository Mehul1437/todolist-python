with open("tasks.txt", "a") as file:
          pass

def add_task():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(f"[ ] {task}\n")
        print("Task added successfully.")

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
        else:
            print("No tasks found.")

def complete_task():
    view_tasks()
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if 0 <= task_num <= len(tasks):
        if "[ ]" in tasks[task_num]:
            tasks[task_num] = tasks[task_num].replace("[ ]", "[x]", 1)
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
            print("Task marked as completed.")
    else:
        print("Invalid task index.")

def delete_task():
    view_tasks()
    task_num = int(input("Enter the task number to delete: ")) - 1

    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if 0 <= task_num <= len(tasks):
        del tasks[task_num]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
            print("Task deleted successfully.")
    else:
        print("Invalid task index.")

while True:
    print("\n ---- To-Do List ---")
    print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Delete Task\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Good Bye!!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
