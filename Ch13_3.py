# 3. Create a class called Shape. Define a method in it called what_am_i that
# prints "I am a shape" when called. Change your Square and Rectangle classes
# from the previous challenges to inherit from Shape, create Square and Rectangle
# objects, and call the new method on both of them.

class Shape():
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, l, w):
        self.length  = l
        self.width   = w

    """Rectangle Perimeter = 2(l+w)"""
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Square(Shape):
    def __init__(self, s):
        self.sides = s

    """Square Perimeter = 4s"""
    def calculate_perimeter(self):
        return 4 * (self.sides)

rec1 = Rectangle(2, 4)
sqr1 = Square(1)

"""Both these statements inherit method from Shape and print the same thing"""
print(rec1.what_am_i())
print(sqr1.what_am_i())