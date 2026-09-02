print("1. Add expense")
print("2. View expense")
print("3. Delete expense")
print("4. Show total")
print("5. Exit")
all_expenses = []
total = 0
while True:
    try:
      user_input = int(input("Choose: "))
    except ValueError:
      print("Invalid choose")
      continue
    if user_input not in range(1, 6):
        print("Invalid option")
        continue
    elif user_input == 1:
            first_question = input("Expense name: ") 
            second_question = int(input("Amount: ")) 
            last_question = input("Category: ")
            all_about_expense = {
                "Expense_name": first_question,
                "Amount" : second_question,
                "Category" : last_question
            }
            all_expenses.append(all_about_expense)
            print("Expense added!")
    elif user_input == 2:
            for number,expenses in enumerate(all_expenses,start=1):
                print(f"{number}. {expenses['Expense_name']} | {expenses['Amount']} | {expenses['Category']}")
    elif user_input == 3:
            delete_expense = int(input("Enter expense number to delete: "))
            if delete_expense in range(1 , len(all_expenses) + 1):
                delete = delete_expense - 1
                all_expenses.pop(delete)
                print("Expense removed!")
            else:
                print("Please enter a valid and right expense number to delete: ")
    elif user_input == 4:
            total = 0
            for expense in all_expenses:
                 amount = expense["Amount"]
                 total += amount
            print(f"{total} TK")
                
    elif user_input == 5:
            exit()