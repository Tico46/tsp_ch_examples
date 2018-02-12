# Write a program with an infinate loop and a list of numbers. (with q to quit)
# Each time through the loop ask the user to guess a number on the list
# and tell them whether or not they guessed correctly.

import time #to use time.sleep(x) where x = seconds

num_list = ["1", "2", "3", "4", "5"]
            

while True:
        print("Type 'q' to quit.")
        guess = input("Take a guess from the number list I've created: ")
        if guess == "q":
                break
        if guess in num_list:
                print("Congrats! You found {}!".format(guess))
                time.sleep(3)
        else:
                print("Sorry, {} is not on the list. Try again!".format(guess))
                time.sleep(3)

# need to factor error handling next time

