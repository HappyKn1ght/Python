'''
1. Write a program to read the text from a given file ‘poems.txtʼ and find out whether it
contains the word ‘twinkleʼ.
'''

# print(open("poems.txt").read())
file = "poems.txt"
with open(file) as f:
    content = f.read()
    if "twinkle" in content:
        print("The word twinkle is present in the content")
    else:
        print("The word twinkle is not present in the content")