# 3. Create a Triangle class with a method called area that
# calculates and returns its area. Then create a Triangle object,
# call area on it, and print the result.

class Triangle():
    def __init__(self, b, h ):
        self.base   = b
        self.height = h
    """Trig Area = 1/2bh"""
    def tri_area(self):
        return 1/2 * (self.base * self.height)

trig1 = Triangle(5, 10)
print(trig1.tri_area())
