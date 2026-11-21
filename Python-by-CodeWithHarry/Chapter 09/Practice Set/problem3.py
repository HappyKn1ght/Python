'''
3. Write a program to generate multiplication tables from 2 to 20 and write it to the different
files. Place these files in a folder for a 13-year-old.
'''
import os

def generate_table(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i}: {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)
    print(f"Generated table_{n}.txt")

os.makedirs("tables", exist_ok=True)
for i in range(2, 21):
    generate_table(i)        