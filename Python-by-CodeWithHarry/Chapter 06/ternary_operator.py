'''
a ternary operator (also known as a conditional expression) allows you to evaluate something based on 
a condition in a single line of code.
'''

age = 20

# Standard if-else
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Ternary operator equivalent
status = "Adult" if age >= 18 else "Minor"

print(status)  # Output: Adult

'''
ternary operator inside print()
score = 85
print("Passed" if score >= 50 else "Failed")  # Output: Passed
'''
