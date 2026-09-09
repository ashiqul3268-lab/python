while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Enter q to quit")
    user_input = input("Choose an operation: ")
    if user_input.lower() == "q":
        break
    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue
    if user_input not in range(1 , 5):
        print("Please enter a valid number.")
        continue
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Please enter a valid number")
            continue
            
    if user_input == 1:
        addition = num1 + num2
        print(f"Result: {addition}")
    elif user_input == 2:
        subtraction = num1 - num2
        print(f"Result: {subtraction}")
    elif user_input == 3:
        multiplication = num1 * num2
        print(f"Result: {multiplication}")
    elif user_input == 4:
        if num2 != 0:
            division = num1 / num2
            print(f"Result: {division}")
        else:
            print("Math error.")