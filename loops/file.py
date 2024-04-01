'''
program file
concept read and write
keywords (file)
Author: AdamsGeeky
Date: 18-03-2024
'''
import os

# read file
filepath = "main.py"
if os.path.exists(filepath):
    with open(filepath) as file:
        print(file.read())
else:
    print(f"File {filepath} does not exist")

# write file
fileName = "hello.txt"

with open(fileName, "w") as file:
    file.write("Hello, World!\n")
    file.write("I love Python!\n")
    file.write("Programming is fun!")
    file.write("I am learning Python")