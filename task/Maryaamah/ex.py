print("========================== Student Result Checker ======================")


# Tuple: Subjects are fixed and should not change
subjects = ("English", "Maths", "Science", "Civics", "Agriculture")


import text 
text.get_text

import integer
integer.get_integer

import grade
grade.calculate_grade

import result
result.calculate_result

def collect_student():

    name = text.get_text(
        "Enter student name: ",
        "Student name"
    )

    age = integer.get_integer(
        "Enter student age: ",
        "Age",
        1,
        100
    )

    department = text.get_text(
        "Enter student department: ",
        "Department"
    )

    # Dictionary: stores one student's information
    student = {
        "name": name,
        "age": age,
        "department": department,
        "scores": []
    }

    # List: stores the student's scores
    for subject in subjects:

        score = integer.get_integer(
            f"Enter {subject} marks: ",
            f"{subject} marks",
            0,
            100
        )

        student["scores"].append(score)

    return student


def display_result(student):

    total, average, grade, result = result.display_result(
        student["scores"]
    )

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


# Get number of students
number_of_students = integer.get_integer(
    "\nHow many students do you want to enter? ",
    "Number of students",
    1
)


# Collect students
for i in range(number_of_students):

    print(f"\n========== Student {i + 1} ==========")

    student = collect_student()

    students.append(student)


# Display all students' results
print("\n\n================ ALL STUDENT RESULTS ================")

for student in students:

    display_result(student)