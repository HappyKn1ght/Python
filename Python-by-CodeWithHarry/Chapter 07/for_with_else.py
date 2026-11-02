'''
l= [1,7,8] 

for item in l:
    print(item)

else:
    print("done") # this is printed when the loop exhausts!
'''

items = ["apple", "banana", "cherry"]

for fruit in items:
    if fruit == "mango":
        print("Found the mango!")
        break
else:
    # This ONLY runs because we checked everything and "mango" wasn't there
    print("Checked the whole store. No mango found.") 
