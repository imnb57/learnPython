### number guessing game using random module
import random

attempts = 0
guess = None
number = random.randint(1,10)

while guess!=number:
    guess = int(input("Enter the number"))
    attempts+=1

    if guess<number:
        print("too low")
    elif guess>number:
        print("too high")
    else :
        print(f"Found on {attempts} attempts!!! ")

