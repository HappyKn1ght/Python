import pyjokes

print("=== WELCOME TO THE JOKE GENERATOR ===")
try:

    # Ask the user how many jokes they want to see
    user_choice = input("How many jokes would you like to hear? ")

    # Convert the user's text input into a whole number (integer)
    number_of_jokes = int(user_choice)

    print("\nHere come your jokes:\n")

    for i in range(number_of_jokes):
        print(f"Joke #{i + 1}: {pyjokes.get_joke()}")
        print("-" * 40) # Prints a clean separator line
except ValueError:
    print("\n❌ Error: Please type an actual digit (like 3), not words!")
print("\nHope you had a laugh! Have a great day!")
