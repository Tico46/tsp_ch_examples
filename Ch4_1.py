# 1. Write a function that takes a number as an input and returns that number squared.

def sqrd(x):
    """
    Returns x squared
    :param x: int
    :return: int x ^ 2
    """
    x = int(x)
    return x**2

x = input("Input a number that you wish to square: ")
print(sqrd(x))
