'''
2. The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file ‘Hi-score.txtʼ which is either blank or contains the previous
Hi-score. You need to write a program to update the Hi-score whenever the game()
function breaks the Hi-score.
'''

import random

def game():
    print("Game Started!")
    score = random.randint(1,100)

    with open("Hi-score.txt") as f:
        hiScore = f.read()
        if hiScore != "":
            hiScore = int(hiScore)
        else:
            hiScore = 0
    print(f"Your Score: {score}")
    if score>hiScore:
        with open("Hi-score.txt", "w") as f:
            f.write(str(score))
    return score

game()