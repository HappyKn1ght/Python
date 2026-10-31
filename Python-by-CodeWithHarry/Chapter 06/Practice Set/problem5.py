# 5. Write a program which finds out whether a given name is present in a list or not.

name_list = ["happy", "harry", "raju", "arpit", "nanu"]

name = input("Enter Name: ").casefold()

if name in name_list:
    print("Your name is in the list")
else:
    print("Your name is not in the list")
