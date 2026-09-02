print("I am thinking of a number between 1 and 100")
import random
secret_number = random.randint(1,100)
low_near_number = secret_number - 10
high_near_number = secret_number + 10
attempt = 0
while True:
    user_input = int(input("guess a number:"))
    attempt += 1
    if  low_near_number <= user_input <= secret_number - 1:
         print(f"your guess : {user_input}")
         print("You are almost there. Try some near high numbers")
    elif secret_number + 1 <= user_input <= high_near_number:
          print(f"your guess : {user_input}")
          print("You are almost there. Try some near low numbers")
    if user_input > high_near_number:
         print(f"your guess : {user_input}")
         print("Greater than the number. Try something low.")
    elif user_input < low_near_number:
         print(f"your guess : {user_input}")
         print("Lower than the the number. Try something high")
    elif user_input == secret_number:
         print(f"🎉 Correct! You got it in {attempt} attempts.")
         break