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
    print(grade)
elif average_marks >= 60:
    grade = "B"
elif average_marks >= 50:
    grade = "C"
elif average_marks >= 45:
    grade = "D"
elif average_marks >= 40:
    grade = "E"
else:   
    grade = "F"
if average_marks >= 40:
    result = "Pass"     
else:
    result = "Fail"
    print(total_marks)
    print(average_marks)

    




