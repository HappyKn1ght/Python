# 6. Write a python function which converts inches to cms.

def inches_to_cms(n):
    return n*2.54

n = int(input("Enter Inch(es): "))
print(f"{n} in = {inches_to_cms(n)} cm")