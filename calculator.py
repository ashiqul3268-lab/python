print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
while True:
    uset_input = input("Choose an operation: ")
    if uset_input.lower() == "q":
        break
    try:
        uset_input = int(uset_input)
    except ValueError:
        print("Please enter a valid number.")
        continue
    if uset_input not in range(1 , 5):
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
            
    if uset_input == 1:
        addition = num1 + num2
        print(f"Result: {addition}")
    elif uset_input == 2:
        substraction = num1 - num2
        print(f"Result: {substraction}")
    elif uset_input == 3:
        multiplication = num1 * num2
        print(f"Result: {multiplication}")
    elif uset_input == 4:
        if num2 != 0:
            division = num1 / num2
            print(f"Result: {division}")
        else:
            print("Math error.")