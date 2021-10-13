import random
from statistics import mean
from statistics import mode
from statistics import median

guess_list = []
def start_game():
    random_num = random.randomint(1, 100)
    guess_count = 0

print("Welcome! To! The! Number! Guessing! Game!")
name = input("What is your name? ")
print("{}, I have picked a number between 1 and 100! You will get to guess that number!".format(name))


    
while player_guess != random_num:
    guess_count += 1
    try:
        player_guess = int(input("Enter your guess now! "))
        if player_guess < 1 or player_guess > 100:
            raise ValueError
        elif random_num > player_guess:
            print("It's lower, try again")
        elif random_num < player_guess:
            print("It's higher, try again")
    except ValueError:
        print("The number you choose, must be between 1 and 100. Try again, please!")
    print("Great job! You got it!")


start_game()
