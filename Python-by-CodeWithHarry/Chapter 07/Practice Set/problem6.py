# 6. Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter Number: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
    # print(i)

print(f"The factorial of {n} is: {factorial}")