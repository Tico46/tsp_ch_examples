# 4. Make a Hexagon class with a method called calculate_perimeter
# that calculates and returns its perimeter. Then create a Hexagon object,
# call calculate_perimeter on it, and print the result.

class Hexagon():
    def __init__(self, s):
        self.sides = s

    """Hexagon perimeter = 6 * sides"""
    def calc_perm(self):
        return 6 * self.sides

hex1 = Hexagon(12)
print(hex1.calc_perm())