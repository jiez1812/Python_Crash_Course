from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

default_die = Die()
for i in range(10):
    print("Roll {0} : {1}".format(i + 1, default_die.roll_die()))

print()

ten_sided_die = Die(10)
for i in range(10):
    print("Roll {0} : {1}".format(i + 1, ten_sided_die.roll_die()))

print()

twenty_sided_die = Die(20)
for i in range(10):
    print("Roll {0} : {1}".format(i + 1, twenty_sided_die.roll_die()))