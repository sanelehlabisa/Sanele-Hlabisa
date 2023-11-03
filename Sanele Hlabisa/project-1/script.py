import random

MAX = 30

print((2 ** 4)*"=","Guess Game",(2 ** 4)*"=")

unkown_number = int(random.random() * MAX)

while True:
    user_input = input(f"\n Guess a integer number between 0 and {MAX} : ")
    if not user_input.isdigit():
        print("Please enter and integer...")
        continue
    user_guess = int(user_input)
    if user_guess == unkown_number:
        print("You guessed correctly")
        break
    else: 
        difference =  user_guess - unkown_number
        print("The number", user_guess, end="")
        if difference > 0.5 * unkown_number:
            print(" is too high")
        elif difference > 0:
           print(" is high")
        elif difference > -0.5 * unkown_number:
            print(" is low")
        else:
            print(" is too low")