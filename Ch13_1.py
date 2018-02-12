# 1. Create Rectangle and Square classes with a method called calculate_perimeter
#  that calculates the perimeter of the shapes they represent. Create Rectangle
# and Square objects and call the method on both of them.

class Rectangle():
    def __init__(self, l, w):
        self.length  = l
        self.width   = w

    """Rectangle Perimeter = 2(l+w)"""
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Square():
    def __init__(self, s):
        self.sides = s

    """Square Perimeter = 4s"""
    def calculate_perimeter(self):
        return 4 * (self.sides)

rec1 = Rectangle(2, 4)
sqr1 = Square(2)

print(rec1.calculate_perimeter())
print(sqr1.calculate_perimeter())
