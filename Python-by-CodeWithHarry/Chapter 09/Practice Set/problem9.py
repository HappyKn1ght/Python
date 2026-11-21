# 9. Write a program to find out whether a file is identical and matches the content of another file

print("this.txt file reading...")
with open("this.txt", "r") as f:
    content1 = f.read()

print("this_copy.txt file reading...")
with open("this_copy.txt", "r") as f:
    content2 = f.read()

if content1 == content2:
    print("Matches found!\nYes this file is identical.")
else:
    print("No matches found!\nNo this file is not identical")