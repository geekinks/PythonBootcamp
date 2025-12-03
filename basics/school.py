from os import system
student_names = []
student_grades = []


def add_student(name, grade):
    student_names.append(name)
    student_grades.append(grade)

def cal_average_grade():
    return sum(student_grades)/len(student_grades)


def diply_students():
    print("\n Student Name and Grades:")
    for name, grade in zip(student_names,student_grades):
        print(f"\t {name} :  {grade}")
          
def clear():
    system("cls")
