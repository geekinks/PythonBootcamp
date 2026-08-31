print("========================== Student Result Checker ======================")

# Tuple: Subjects are fixed and should not change
subjects = ("English", "Maths", "Science", "Civics", "Agriculture")


def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def calculate_result(scores):
    total = sum(scores)
    average = total / len(scores)

    grade = calculate_grade(average)

    if average >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return total, average, grade, result


def collect_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    department = input("Enter student department: ")

    # Dictionary: stores one student's information
    student = {
        "name": name,
        "age": age,
        "department": department,
        "scores": []
    }

    # List: stores the student's multiple scores
    for subject in subjects:
        score = int(input(f"Enter {subject} marks: "))
        student["scores"].append(score)

    return student


def display_result(student):
    total, average, grade, result = calculate_result(student["scores"])

    print("\n================ STUDENT RESULT ================")
    print(f"Name:        {student['name']}")
    print(f"Age:         {student['age']}")
    print(f"Department:  {student['department']}")
    print("-----------------------------------------------")

    # Loop through subjects and scores
    for subject, score in zip(subjects, student["scores"]):
        print(f"{subject}:       {score}")

    print("-----------------------------------------------")
    print(f"Total Marks:    {total}")
    print(f"Average Marks:  {average:.2f}")
    print(f"Grade:          {grade}")
    print(f"Result:         {result}")
    print("================================================")


# List: stores multiple students
students = []

number_of_students = int(input("\nHow many students do you want to enter? "))

for i in range(number_of_students):
    print(f"\n========== Student {i + 1} ==========")

    student = collect_student()
    students.append(student)


# Display all students' results
print("\n\n================ ALL STUDENT RESULTS ================")

for student in students:
    display_result(student)
