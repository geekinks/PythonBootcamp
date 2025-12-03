from welcome import greeting, goodbye
from school import add_student, cal_average_grade, display_students, student_names

greeting("Adamu")
while True:
    print("\n Option: ")
    print("1. Add Student ")
    print("2. calculate Avarage Grade ")
    print("3. Display Students ")
    print("4. Exit")

    choice = input("Enter your Choice")

    if choice == '1':
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        add_student(name, grade)
        print("Student added successfully")

    elif choice == '2':
        if len(student_names) == 0:
            print("No students added yet")
        else:
            print(f"Average grade: {cal_average_grade()}")

    elif choice == '3':
        if len(student_names) == 0:
            print("No students added yet")
        else:
            display_students()
    elif choice == '4':
        goodbye()
        break
    else:
        print("Invalid choice the Options are: 1, 2, 3, 4")




    
    
