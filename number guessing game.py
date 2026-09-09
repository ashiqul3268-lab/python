import random
print("I am thinking between 1 and 100")
secret_number = random.randint(1,100)
near_low_number = secret_number - 10
near_low_number = max(near_low_number,1)
near_high_number = secret_number + 10
near_high_number = min(near_high_number,100)
attempt = 0
while True:
    try:
       user_input_number = int(input("Guess a number: "))
    except ValueError:
        print("Enter a valid number.")
        continue
    if user_input_number not in range(1,101):
        print("Enter a valid number.")
        continue
    attempt += 1
    if near_low_number <= user_input_number < secret_number:
        print(f"your guess : {user_input_number}")
        print("You are almost there. Try some near high numbers.")
    elif near_high_number >= user_input_number > secret_number:
        print(f"your guess : {user_input_number}")
        print("You are almost there. Try some near low numbers.")
    elif user_input_number < near_low_number:
        print(f"your guess : {user_input_number}")
        print("Lower than the secret number. Try some high numbers.")
    elif user_input_number > near_high_number:
        print(f"your guess : {user_input_number}")
        print("Greater than the secret number. Try some low numbers")
    elif user_input_number == secret_number:
        print(f"🎉Correct! You got it in {attempt} attempts")
        break