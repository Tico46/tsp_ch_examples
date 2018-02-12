# Create a module named "cube with a function that takes a number as a parameter,
# and returns the number cubed. Import and call the function from another module.

import mathAssist



try:
    x = int(input("Please input a number that you would like cubed: "))
    y = mathAssist.cubed(x)
    print(y)
except ValueError:
    print("I'm sorry, that is not a number!")

    
