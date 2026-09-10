total_balance = 0
transactions = []
while True:
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. View transaction history")
    print("5. Exit")
    try:
        user_input = int(input("Choose: "))
    except ValueError:
        print("Enter a valid number.")
        continue
    if user_input not in range(1,6):
        print("Enter a valid number.")
        continue
    if user_input == 2:
        while True:
            try:
               amount = int(input("Enter deposit amount: "))
            except ValueError:
               print("Enter a valid amount.")
               continue
            if amount <= 0:
                print("Enter a valid amount.")
                continue
            break
        total_balance += amount
        transactions.append(f"Deposit: {amount}")
        print("Deposit successful!")
    elif user_input == 1:
        print(f"Balance: {total_balance}Tk")
    elif user_input == 3:
        while True:
            try:
               withdraw_amount = int(input("Enter withdraw amount: "))
            except ValueError:
               print("Enter a valid amount.")
               continue
            if withdraw_amount <= 0:
                print("Enter a valid amount.")
                continue
            break
        if total_balance >= withdraw_amount:
            total_balance -= withdraw_amount
            transactions.append(f"Withdraw: {withdraw_amount}")
            print("Withdraw successful!")
        else:
            print("Insufficient balance!")
    elif user_input == 4:
        # if transactions == []:
        if not transactions:
            print("No transactions yet!")
        else:
           for transaction_history in transactions:
                print(transaction_history)
    elif user_input == 5:
        exit()