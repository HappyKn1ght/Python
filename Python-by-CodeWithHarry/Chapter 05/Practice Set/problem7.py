# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
# ans: The values entered later will be updated

dict = {}

name = input("Enter Friend Name: ")
lang = input("Enter Language: ")
dict.update({name: lang})

name = input("Enter Friend Name: ")
lang = input("Enter Language: ")
dict.update({name: lang})

name = input("Enter Friend Name: ")
lang = input("Enter Language: ")
dict.update({name: lang})

name = input("Enter Friend Name: ")
lang = input("Enter Language: ")
dict.update({name: lang})

print(dict)