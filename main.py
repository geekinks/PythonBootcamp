
import os

student_names = []
student_grades = []


def add_student(name, grade):
    student_names.append(name)
    student_grades.append(grade)


def calculate_average_grade():
    if student_grades:
        return sum(student_grades) / len(student_grades)
    else:
        return 0  # return 0 if no grades are available


def display_students():
    print("\nStudent Name and Grades:")
    for name, grade in zip(student_names, student_grades):
        print(f"\t{name} : {grade}")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def save_data():
    with open("student_data.txt", "w") as file:
        for name, grade in zip(student_names, student_grades):
            file.write(f"{name},{grade}\n")


def load_data():
    if os.path.exists("student_data.txt"):
        with open("student_data.txt", "r") as file:
            for line in file:
                name, grade = line.strip().split(",")
                add_student(name, float(grade))


def goodbye():
    save_data()
    print("Data saved successfully!")


def main():
    load_data()
    while True:
        clear()
        print("\nOptions:")
        print("1. Add Student")
        print("2. Calculate Average Grade")
        print("3. Display Students")
        print("4. Exit")

        choice = input("Enter your Choice: ")

        if choice == '1':
            name = input("Enter Student name: ")
            while True:
                grade = input("Enter Student Grade: ")
                try:
                    grade = float(grade)
                    break
                except ValueError:
                    print("Please enter a valid number for the grade.")
            add_student(name, grade)
            print("Student Added Successfully!")
        elif choice == '2':
            average = calculate_average_grade()
            print(f"Average Grade is {average}")
        elif choice == '3':
            display_students()
        elif choice == '4':
            print("Thank you for using Grade Management System")
            goodbye()
            clear()
            break
        else:
            print("Invalid choice. Please enter a valid option (1, 2, 3, 4)")
            clear()


if __name__ == "__main__":
    main()
