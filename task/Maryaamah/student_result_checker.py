print("==========================Student Result Checker======================")

name = input ("Enter your name: ")
age = int (input ("Enter your age: "))
department = input ("Enter your department: ")

English = int(input ("Enter your English marks: "))
Maths = int(input ("Enter your Maths marks: "))
Science = int(input ("Enter your Science marks: "))
civics = int(input ("Enter your Civics marks: "))
agriculture = int (input ("Enter your Agriculture marks: "))


total_marks = English + Maths + Science + civics + agriculture
average_marks = total_marks / 5

if average_marks >= 70:
    grade = "A"
    print(f"Grade: {grade}")
elif average_marks >= 60:
    grade = "B"
    print(f"Grade: {grade}")
elif average_marks >= 50:
    grade = "C"
    print(f"Grade: {grade}")
elif average_marks >= 45:
    grade = "D"
    print(f"Grade: {grade}")
elif average_marks >= 40:
    grade = "E"
    print(f"Grade: {grade}")
else:   
    grade = "F"
    print(f"Grade: {grade}")
if average_marks >= 40:
    result = "Pass"     
else:
    result = "Fail"
print("              ")

print(f"name: {name}")
print(f"age: {age}")
print(f"department: {department}")
print("              ")

print(f"English: {English}")
print(f"Maths: {Maths}")
print(f"Science: {Science}")
print(f"Civics: {civics}")
print(f"Agriculture: {agriculture}")
print("              ")

print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Grade: {grade}")
print(f"Result: {result}")


