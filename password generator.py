import random
import string
print("Enter q to quit.")
while True:
    user_input = input("How long the password should be? ")
    if user_input.lower() == "q":
        exit()
    try:
        user_input = int(user_input)
    except ValueError:
        print("Please input a valid number.")
        continue
    if user_input <= 0:
        print("Enter a positive whole number")
        continue
    if user_input > 20:
        print("Enter a number in 20")
        continue
    break
numbers = string.digits
letters = string.ascii_letters
punctuations = string.punctuation
password = numbers + letters + punctuations
generated_password = ""
#for x in range(user_input):
#    generated_password += random.choice(password)
generated_password = "".join(random.choice(password) for _ in range(user_input))
print(f"Generated password: {generated_password}")