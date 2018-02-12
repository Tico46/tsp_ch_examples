# Game to guess if item is in a list

colors = ["red", "orange", "yellow", "green", "purple", "blue", "white"]

guess = input("Guess a color on the list: ")

if guess in colors: # "in" is keyword to check if item is on list
    print("You got it!", guess, "is in the list!")
else:
    print("Sorry,", guess, "is not on the list! Try again!")
