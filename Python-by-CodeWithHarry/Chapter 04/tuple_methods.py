a = (1,45,342,3424,False, 45, "Raju", "Arpit")
print(a) 

no = a.count(45) # a.count(45): a count (45) will return number of times 45 occurs in a.
print(no)

i = a.index(3424) # a.index(3424) will return the index of first occurrence of 3424 in a.
print(i)

print(len(a))

print("Raju" in a)
print(9 in a)

sliced = a[6:8] # tuple slicing
print(sliced)