print("==========================Student Result Checker======================")

def result_checker():
    student = {
        "name": input("Enter your name: "),
        "age": int(input("Enter your age: ")),
        "department": input("Enter your department: ")
    }

    subjects = ["English", "Maths", "Science", "Civics", "Agriculture"]

    marks = {}
    for subject in subjects:
        marks[subject] = int(input(f"Enter your {subject} marks: "))

    total_marks = sum(marks.values())
    average_marks = total_marks / 5


    if average_marks >= 70:
        grade = "A"
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

    
    print("              ")
    print(f"name: {student['name']}")
    print(f"age: {student['age']}")
    print(f"department: {student['department']}")

    print("              ")

    for subject in subjects:
        print(f"{subject}: {marks[subject]}")

    print("              ")

    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks}")
    print(f"Grade: {grade}")
    print(f"Result: {result}")


result_checker()