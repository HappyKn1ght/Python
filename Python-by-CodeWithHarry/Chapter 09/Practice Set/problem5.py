# 5. Repeat program 4 for a list of such words to be censored.

file = "donkey.txt"
words = ["Donkey", "Bad", "Shit"]
with open(file, "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open(file, "w") as f:
    f.write(content)

print(content)
