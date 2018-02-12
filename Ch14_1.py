# 1. Add a square_list class variable to a class called Square so that every time you create a new Square object,
# the new object gets added to the list.

class Square():
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)

# Loop to test functionality of appending to class variable
for i in range(5):
    sqr1 = Square(i)
    i += 1

print(Square.square_list)

