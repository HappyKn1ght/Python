# 1. Write a program using functions to find greatest of three numbers.

#function definiton
def find_max(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

a = int(input("Enter Num1: "))
b = int(input("Enter Num2: "))
c = int(input("Enter Num3: "))

#function call
print("Max:",find_max(a,b,c))