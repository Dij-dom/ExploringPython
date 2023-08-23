tasks = []
def display():
    if tasks:
        print("\nYour saved tasks are:")
        for index, task in enumerate(tasks, start = 1):
            print(f"{index}.{tasks[index-1]}")
    else:
        print("You have completed every tasks. Go and chill mahnn!!")

def add_tasks():
    task =input("Enter the task\n")
    tasks.append(task)
    print("Task added successfully.")

def com_task():
    display()
    if tasks:
        task_index = int(input("\nEnter the task number to mark as complete."))
        if task_index<=len(tasks):
            com_task = tasks[task_index-1] 
            com_tasks = tasks.pop(task_index-1)
            print(f"Completed task: {com_task}")
        else:
            print("Invalid Task entry.")
    else:
        print("No task to complete.")
    
while True:
    print("\nTo Add Tasks press 1\n"+ "To display your Tasks Press 2\n" + "To mark a task as complete Press 3\n"+ "To Close Task Manager Press 4\n")
    ch = int(input("Enter your choice\n"))
    while ch>4  or ch<1:
        ch = int(input("Enter a valid choice\n"))
    if ch == 1:
        add_tasks()
    elif ch == 2:
        display()
    elif ch == 3:
        com_task()
    else:
        break
    
