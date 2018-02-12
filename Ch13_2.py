# 2. Define a method in your Square class called change_size that allows you to
# pass in a number that increases or decreases (if the number is negative) each
# side of a Square object by that number.

class Square():
    def __init__(self, s):
        self.sides = s

    """change the length of sides"""
    def change_size(self, chg):
        self.sides += chg

    """Square Perimeter = 4s"""
    def calculate_perimeter(self):
        return 4 * (self.sides)

sqr1 = Square(5) #Initiates the sides as 5
print(sqr1.sides)

sqr1.change_size(-5) #Changes the size of sides
print(sqr1.sides)
