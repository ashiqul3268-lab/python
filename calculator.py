print("1. addition")
print("2. substraction")
print("3. multiplication")
print("4. division")
operator = int(input("chose an operation :"))
if operator not in range(1,5):
    print("invalid operation")
    exit()
num1 = float(input("enter first number :"))
num2 = float(input("enter second number :"))

if operator == 1:
    addition = num1 + num2
    print(f"result : {addition}")
elif operator == 2:
    substraction = num1 - num2
    print(f"result : {substraction}")
elif operator == 3:
    multiplication = num1 * num2
    print(f"result : {multiplication}")
elif operator == 4:
    if num2 != 0:
        division = num1 / num2 
        print(f"result : {division}")
    else:
        print("math error")