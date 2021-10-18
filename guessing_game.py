import random
import math
from statistics import mean
from statistics import mode
from statistics import median


random_num = random.randint(1, 100)
guess_count = 0
player_guess = 0

guess_list = []
def start_game():
    print("")
name = input("Welcome! To! The! Number! Guessing! Game! What is your name? ")
print("{}, I have picked a number between 1 and 100! You will get to guess that number! Let's go.".format(name))

   
while player_guess != random_num:
    guess_count += 1
    try:
        player_guess = int(input("Enter your guess now! "))
        if player_guess < 1 or player_guess > 100:
            raise ValueError
        elif random_num < player_guess:
            print("It's lower, try again")
        elif random_num > player_guess:
            print("It's higher, try again")
        elif random_num == player_guess:
            print("You got it!")
        ## add below to test the list of scores    
            print(guess_list)
    except ValueError:
        print("The number you choose, must be between 1 and 100. Try again, please!")
    
print("Here is how you did!\nIt took you {} tries to guess the correct number.".format(guess_count))
guess_list.append(guess_count)
print("Mean Guess: {}".format(mean(guess_list)))
print("Median Guess: {}".format(median(guess_list)))
print("Mode Guess: {}".format(mode(guess_list)))

play_again = input("Would you like to play again? Type Y or N. ")
if play_again == 'N':
    print("Thanks for playing! We hope you had fun.")
else:
    start_game()
        
    
start_game()
