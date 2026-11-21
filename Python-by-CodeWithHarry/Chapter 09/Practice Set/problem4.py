'''
4. A file contains a word “Donkey” multiple times. You need to write a program which
replaces this word with ###### by updating the same file.
'''

file = "donkey.txt"
word = "Donkey"
with open(file, "r") as f:
    content = f.read()

content = content.replace(word, "#" * len(word))

with open(file, "w") as f:
    f.write(content)

print(content)