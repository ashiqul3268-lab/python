print("1. Add task")
print("2. View tasks")
print("3. Remove task")
print("4. Exit")
tasks = []
while True:
    user_input = int(input("Choose an option: "))
    if user_input not in range(1,5):
        print("Invalid option")
    elif user_input == 1:
        tasks.append(input("Enter task: "))
        print("Task added!")
    elif user_input == 2:
        for number , all_task in enumerate(tasks, start=1):
            print(f"{number}. {all_task}")
    elif user_input == 3:
        remove_task = int(input("Enter task number to remove: "))
        if remove_task in range(1,len(tasks) + 1):
           remove_index = remove_task - 1
           tasks.pop(remove_index)
           print("Task removed!") 
        else:
            print("Invalid task number")
    elif user_input == 4:
        exit()