# Snake Water Gun Game

import random

print("Snake Water Gun Game")
print("1 for Snake\n2 for Water\n3 for Gun")

choice = {1: "Snake", 2: "Water", 3: "Gun"}

while True:

    user_input = input("Enter Your Choice or 'q' to quit: ").lower().strip()
    if user_input == "q":
        print("\nGAME OVER...\nThanks for playing!")
        break

    try:
        user_input = int(user_input)
        if user_input not in choice:
            print("Out of range! Please choose 1, 2, or 3.")
            continue
        print(f"You chose {choice[user_input]}")
        computer = random.randint(1, 3)
        print(f"Computer Chose {choice[computer]}")

        if user_input == computer:
            print(f"Both Chose {choice[user_input]}\nIt's a draw!")

        elif (
            (user_input == 1 and computer == 2)
            or (user_input == 2 and computer == 3)
            or (user_input == 3 and computer == 1)
        ):
            print("You Win!")
        else:
            print("Computer Wins!")
    except ValueError:
        print("Invalid Input!")
        continue

    again = input("Do you want to try again? (y/n): ").lower().strip()
    if again != "y":
        print("\nGAME OVER...\nThanks for playing!")
        break
