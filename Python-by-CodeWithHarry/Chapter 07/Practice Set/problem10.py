# 10. Write a program to print multiplication table of n using for loops in reversed order.
# using while loop
n = int(input("Enter N: "))
i = 10
print("Using while loop:")
while i >= 1:
    print(f"{n} X {i} = {n*i}") 
    i -= 1

#using for loop
print("Using for loop:")

for i in range(10, 0, -1):
    print(f"{n} X {i} = {n*i}") 