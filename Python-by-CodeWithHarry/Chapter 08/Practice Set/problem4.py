# 4. Write a recursive function to calculate the sum of first n natural numbers.
understand this!
def sum_of_n_recursive(n):
    # 1. BASE CASE
    if n <= 1:
        return 1
        
    # 2. RECURSIVE CASE (The function calls ITSELF!)
    else:
        return n + sum_of_n_recursive(n - 1)

n = int(input("Enter N: "))
print(f"The sum is: {sum_of_n_recursive(n)}")
