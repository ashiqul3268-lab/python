print("1. Check balance")
print("2. Deposite money")
print("3. Withdraw money")
print("4. View transaction history")
print("5. Exit")
balance = 0
transactions = []
while True:
    try:
        user_input = int(input("Choose: "))
    except ValueError:
        print("Enter a valid number")
        continue
    if user_input not in range(1 ,6):
        print("Enter a valid number")
    elif user_input == 2:
        deposite_amount = int(input("Enter amount: "))
        balance += deposite_amount
        transactions.append(f"Deposit: {deposite_amount}Tk")
        print("Deposite successful!")
    elif user_input == 1:
        print(f"Balance: {balance}Tk")
    elif user_input == 3:
        withdraw_amount = int(input("Enter amount: "))
        if balance >= withdraw_amount:
          balance -= withdraw_amount
          transactions.append(f"Withdrawal: {withdraw_amount}Tk")
        else:
            print("Insufficient balance!")
    elif user_input == 4:
        for history in transactions:
          print(history)
    elif user_input == 5:
        exit()
    