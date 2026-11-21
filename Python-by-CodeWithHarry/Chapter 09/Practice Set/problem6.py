# 6. Write a program to mine a log file and find out whether it contains ‘pythonʼ.

with open("log.txt", "r") as f:
    content = f.read()
    # print("python" in content)
if "python" in content.lower():
    print("Yes, 'python' is present in the log file.")
else:
    print("No, 'python' is not present in the log file.")
  