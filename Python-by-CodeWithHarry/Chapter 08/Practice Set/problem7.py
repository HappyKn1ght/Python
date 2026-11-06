# 7. Write a python function to remove a given word from a list and strip it at the same time.

# word_list = ["happy", "sad", "Joy", "angry", "smile"]

# print(f"Original list:-\n{word_list}")
# word = input("Enter Word to remove from the list: ")
# word_list.remove(word)
# print(f"{word} remove from the list\nNew list:-\n{word_list}")

def remove_list(word):
    return word_list.remove(word)

word_list = ["happy", "sad", "Joy", "angry", "smile"]

print(f"Original list:-\n{word_list}")
word = input("Enter Word to remove from the list: ")

print(f"{word} remove from the list\nNew list:-\n{remove_list(word)}")