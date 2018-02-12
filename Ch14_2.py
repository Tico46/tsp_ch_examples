# 2. Change the Square class so that when you print a Square object, a message prints telling you
# the len of each of the four sides of the shape. For example, if you create a square with
# Square(29) and print it, Python should print 29 by 29 by 29 by 29.

class Square():
    def __init__(self, s):
        self.side = s


    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)

sqr1 = Square(29)

print(sqr1)