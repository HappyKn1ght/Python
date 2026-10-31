# 4. Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter username: ")

if len(username) < 10:
    print("Yes, the username contains less than 10 characters.")
else:
    print("No, the username contains 10 or more characters.")
