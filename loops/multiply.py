'''
program for loops
concept loops(for)
keywords (for, in, range)
Author: AdamsGeeky
Date: 18-03-2024
'''

# function definition
def generate_table(num):
    for i in range(1, 11):
        print(f"{i} * {num} = {num * i}")
   

if __name__ == "__main__":
    # call only function
    generate_table(5)