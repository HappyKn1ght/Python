'''1. Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!
'''

dict = {
    "madad" : "help",
    "khush" : "happy",
    "dukh" : "sad",
    "seb" : "apple",
    "kela" : "banana",
    "madad": "Help",
    "kursi": "Chair",
    "billi": "Cat",
    "bharat" : "india"
}

word = input("Enter the hindi word you in english: ")
print("Hindi  English")
print(f"{word}: {dict[word]}")