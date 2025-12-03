'''
program student recod
concept list
keywords []
Author: AdamsGeeky
Date: 19-03-2024
'''

# 5 Student
# 1. AdamsGeeky
# 2. Ali
# 3. Inuwa
# 4. ibrahim
# 5. Adamu

# std1 = "AdamsGeeky"
# std2 = "Ali"
# std3 = "Inuwa"
# std4 = "ibrahim"
# std5 = "Adamu"

# print(std1)
# print(std2)
# print(std3)
# print(std4)
# print(std5)

# list of students
students = ["AdamsGeeky", "Ali", "Inuwa", "ibrahim", "Adamu"]

# access all
print(students)

# add
students.append("Salamu")
print(students)

# remove
students.remove("Inuwa")
print(students)

# length
print(len(students))

# remove last
students.pop()
print(students)


# access specific
for x in students:
    print(x)