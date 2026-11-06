# 2. Write a python program using function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(c):
    f = ((c*1.8) + 32)
    return f # return ((c*1.8) + 32) 

n = int(input("Enter Celsius: ")) 
print(f"{n}°C in fahrenheit: {celsius_to_fahrenheit(n)}°F")