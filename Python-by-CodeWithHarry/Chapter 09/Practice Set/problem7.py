# 7. Write a program to find out the line number where python is present from ques 6.

with open("log.txt", "r") as f:
    lines = f.readlines()
lineno = 1
found = False
for line in lines:
    if "python" in line.lower():
        print(f"Yes, 'python' is present in the log file line no {lineno}.")
        found = True
        
    lineno += 1
if not found:
    print("No, 'python' is not present in the log file.")
  