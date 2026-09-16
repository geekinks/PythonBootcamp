from functions import (
    get_integer,
    collect_student,
    display_result
)

print("========================== Student Result Checker ======================")

# List: stores multiple students
students = []


# Get number of students
number_of_students = get_integer(
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