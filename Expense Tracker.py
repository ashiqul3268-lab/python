all_expenses = []
total = 0
while True:
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Show total")
    print("5. Exit")
    while True:
        try:
            user_input = int(input("Choose an option: "))
        except ValueError:
            print("Enter a valid number.")
            continue
        if user_input not in range(1, 6):
            print("Enter a valid number.")
            continue
        break
    if user_input == 1:
        first_question = input("Expense name: ")
        while True:
            try:
               second_question = int(input("Amount: "))
            except ValueError:
                print("Enter a valid amount.")
                continue
            if second_question <=0 :
                print("Enter a valid amount.")
                continue
            break
        third_question = input("Category: ")
        all_about_expenses ={
            "Expense_name" : first_question,
            "Amount" : second_question,
            "Category" : third_question
        }
        all_expenses.append(all_about_expenses)
        print("Expense added.")
    elif user_input == 2:
        if not all_expenses:
            print("NO expense added yet!")
        for number,expenses in enumerate(all_expenses, start=1):
            print(f"{number}. Expense: {expenses['Expense_name']} | Amount: {expenses['Amount']} | Category: {expenses['Category']} |")
    elif user_input == 3:
        while True:
            try:
                remove_task = int(input("Enter task number to remove: "))
            except ValueError:
                print("Enter a valid number.")
                continue
            break
        if remove_task in range(1, len(all_expenses) + 1):
            delete_expense = remove_task - 1
            all_expenses.pop(delete_expense)
        else:
            print("Enter a valid number.")
    elif user_input == 4:
        total = 0
        for total_expense in (all_expenses):
            total += total_expense['Amount']
        print(f"Total: {total}Tk")
    elif user_input == 5:
        exit()