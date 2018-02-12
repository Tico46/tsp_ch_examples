# 4. Write a program with two functions. The first function should take an integer as a
# parameter and return the result of the integer divided by 2. The second function should
# take an integer as a parameter and return the result of the integer multiplied by 4.
# Call the first function, save the result as a variable, and pass it as a parameter to the
# second function.

def division (x): # Will take an integer as parameter and return (int/2)
    x = int(x)
    return x/2

def multiply (x): # Will take an int as param and return result of (int * 4)
    x = int(x)
    return x * 4

div_result = division(8)

print(multiply(div_result))

