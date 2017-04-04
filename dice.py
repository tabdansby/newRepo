import random

dice = int(input('How many dice do you want to roll? <<'))
sides =  int(input('How many sides do you want on each die?<<'))

for i in range(0, dice):
    roll = random.randint(1, sides)
    print(roll)

# for dice:
#     choice = random.randint(dice, sides)
#
# print(choice)
