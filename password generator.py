try:
   user_input = int(input("How long should the password be? "))
except ValueError:
   print("invalid input please enter a whole number")
   exit()
import random
import string
number = string.digits
letter = string.ascii_letters
punctuation = string.punctuation
password = number + letter + punctuation
if user_input <= 0:
  print("Invalid password length")
  exit()
generated_password = ""
for x in range(user_input):
    generated_password += random.choice(password)
print(f"Generated password: {generated_password}")