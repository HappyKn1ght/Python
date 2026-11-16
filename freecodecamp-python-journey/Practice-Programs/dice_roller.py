import random
while True:
    Dice = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    dice = random.choice(Dice)
    print("dice: ", dice)
    #dice = random.randint(1,6)
    #print("dice: ", dice)
    again = input("roll the dice again (y/n): ").lower().strip()
    if again != 'y':
        break
