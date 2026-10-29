'''2. Write a program to fill in a letter template given below with name and date.
letter = 
Dear <|Name|>,
You are selected!
<|Date|>
'''

user_name = input("Enter the name: ")
user_date = input("Enter the date: ")

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

final_letter = letter.replace("<|Name|>", user_name.title()).replace("<|Date|>", user_date)

print(final_letter)
