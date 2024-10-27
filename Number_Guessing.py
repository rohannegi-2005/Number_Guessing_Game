import random 
from art import logo_2
def random_number():
    number = random.randint(0,100)
    return number

#Introduction
print(logo_2)
print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100.")

#Creating a variable ask_user so that we known when to end the game.
ask_user = 0
while (ask_user == 0):
# Asking user the difficulty level.
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == 'easy':
        attempts = 10
    elif level == 'hard':
        attempts = 5
# Get a random number using random module and store it in variable named as target_number.
    terget_number = random_number()

    
# Number Checking Process.
    for _ in range(attempts):
        Guess_number = int(input("Make a guess."))
        if (Guess_number + 10) < terget_number:
            print("Too low")
            attempts = attempts - 1
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif (Guess_number - 10) > terget_number:
            print("Too high")
            attempts = attempts - 1
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif Guess_number > terget_number:
            print("high but close")
            attempts = attempts - 1
            print(f"You have {attempts} attempts remaining to guess the number.")   
        elif Guess_number < terget_number:
            print("low but close")
            attempts = attempts - 1
            print(f"You have {attempts} attempts remaining to guess the number.")    
        else:
            print("You won")
            break
    if attempts == 0:
        print("You've run out of attempts! The number was:", terget_number)

# Asking user to play further more or not.
    ask_user = input("Do you wanna play it again? Type yes or no.")
    if (ask_user == 'yes'):
        ask_user = 0
    else:
        print("OKAY THANKYOU, Have a Nice Day!")
        ask_user = 1
