tasks = []
while True:
    print("1. Add task")
    print("2. View task")
    print("3. Remove task")
    print("4. Exit")
    while True:
        try:
            user_input = int(input("Choose an option: "))
        except ValueError:
            print("Enter a valid number.")
            continue
        if user_input not in range(1, 5):
            print("Enter a valid number.")
            continue
        break
    if user_input == 1:
        add_task = input("Enter task: ")
        tasks.append(add_task)
        print("Task added!")
    elif user_input == 2:
        if not tasks:
            print("NO tasks yet!")
        for number,all_task in enumerate(tasks, start=1):
            print(f"{number}. {all_task}")
    elif user_input == 3:
        while True:
            try:
               remove_task = int(input("Enter task number to remove: "))
            except ValueError:
                print("Enter a valid number.")
                continue
            break
        if remove_task in range(1, len(tasks) +1):
            delete_task = remove_task -1
            tasks.pop(delete_task)
            print("Task removed!")
        else:
            print("Enter a valid number.")
    elif user_input == 4:
        exit()