print("========================== Student Result Checker ======================")


# Tuple: Subjects are fixed and should not change
subjects = ("English", "Maths", "Science", "Civics", "Agriculture")


def get_text(prompt, field_name):
    """Get valid text input from the user."""

    while True:
        value = input(prompt).strip()

        # Check if input is empty
        if not value:
            print(f"Error: {field_name} cannot be empty.")
            continue

        # Check if input contains only numbers
        if value.isdigit():
            print(f"Error: {field_name} must contain text, not numbers.")
            continue

        return value


def get_integer(prompt, field_name, minimum=None, maximum=None):
    """Get a valid integer from the user."""

    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Error: {field_name} must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Error: {field_name} must not exceed {maximum}.")
                continue

            return value

        except ValueError:
            print(f"Error: Please enter a valid number for {field_name}.")


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

    name = get_text(
        "Enter student name: ",
        "Student name"
    )

    age = get_integer(
        "Enter student age: ",
        "Age",
        1,
        100
    )

    department = get_text(
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

        score = get_integer(
            f"Enter {subject} marks: ",
            f"{subject} marks",
            0,
            100
        )

        student["scores"].append(score)

    return student


def display_result(student):

    total, average, grade, result = calculate_result(
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