# 5. Write a function that converts a string to a float and returns the result.
# Use exception handling to catch the exception that could occur.

# This function will take x as param and convert to float. Will handle errors as well
def str_to_float(float_val):
    float_val = float(float_val)
    return float_val

float_val = input("Please enter a number you would like to convert to float: ")
try:
    print(str_to_float(float_val))
except ValueError:
        print("Value must be of int or float type")
