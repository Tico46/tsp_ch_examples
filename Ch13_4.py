# 4. Create a class called Horse and a class called Rider. Use composition to
# model a horse that has a rider.

class Horse():
    def __init__(self, c, b, nickname, o):
        self.color = c
        self.breed = b
        self.nickn = nickname
        self.owner = o


class Rider():
    def __init__(self, n):
        self.name = n

rider_1 = Rider("Joe Smith")
horse_1 = Horse("brown", "Mustang", "Speedy", rider_1)

print("We are proud to present {}, the {} {}."
      .format(horse_1.nickn, horse_1.color, horse_1.breed))
print("The owner of this wonderful horse is {}.".format(horse_1.owner.name))
