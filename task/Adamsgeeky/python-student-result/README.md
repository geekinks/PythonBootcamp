# 🐍 Python Practical Assignment: Student Result Checker

## 📌 Overview

This practical assignment is designed to test your understanding of basic Python programming concepts, especially:

* Data Types
* Variables
* User Input
* Conditional Statements
* Loops
* Lists
* Basic Arithmetic Operations

You are expected to build a simple **Student Result Checker** using Python.

> **Important:** Do not copy a solution from the internet or another student. The goal of this assignment is to demonstrate your own understanding.

---

## 🎯 Learning Objectives

By completing this assignment, you should be able to:

1. Use different Python data types correctly.
2. Store and manipulate data using variables.
3. Collect information from a user.
4. Use `if`, `elif`, and `else` statements.
5. Use loops to repeat tasks.
6. Store multiple values inside a list.
7. Perform basic calculations.
8. Combine multiple Python concepts to solve a practical problem.

---

# 📝 Assignment

Create a Python program called:

```text
student_result_checker.py
```

Your program should collect information about a student and calculate their academic performance.

---

## 1. Collect Student Information

Ask the user to enter:

* Student Name
* Age
* Department

Example:

```text
Enter your name: Ahmad
Enter your age: 22
Enter your department: Computer Science
```

Make sure you use appropriate data types.

For example:

* Name → `str`
* Age → `int`
* Department → `str`

---

## 2. Collect Five Subject Scores

Your program should collect the scores for **5 subjects**.

You **must use a loop** to collect the scores.

Example:

```text
Enter score for subject 1: 75
Enter score for subject 2: 68
Enter score for subject 3: 81
Enter score for subject 4: 59
Enter score for subject 5: 72
```

Store the scores inside a **list**.

Example:

```python
scores = []
```

---

## 3. Calculate the Total

Calculate the total score of the five subjects.

For example:

```text
75 + 68 + 81 + 59 + 72 = 355
```

The program should display:

```text
Total: 355
```

---

## 4. Calculate the Average

Calculate the student's average score.

Formula:

```text
Average = Total Score / Number of Subjects
```

Example:

```text
Average: 71.0
```

The average should be stored as a numeric value that can represent decimals.

---

# 5. Determine the Grade

Use `if`, `elif`, and `else` statements to determine the student's grade.

| Average Score | Grade |
| ------------: | :---: |
|      70 – 100 |   A   |
|       60 – 69 |   B   |
|       50 – 59 |   C   |
|       45 – 49 |   D   |
|       40 – 44 |   E   |
|      Below 40 |   F   |

Your program should display the appropriate grade.

Example:

```text
Grade: A
```

---

# 6. Determine Pass or Fail

Use a condition to determine whether the student passed.

Rules:

```text
Average >= 40 → Passed
Average < 40 → Failed
```

Example:

```text
Status: Passed
```

---

# 7. Display the Final Result

Your program should produce a clear result similar to:

```text
==============================
       STUDENT RESULT
==============================

Name: Ahmad
Age: 22
Department: Computer Science

Scores:
Subject 1: 75
Subject 2: 68
Subject 3: 81
Subject 4: 59
Subject 5: 72

Total: 355
Average: 71.0
Grade: A
Status: Passed

==============================
```

Your design does not have to look exactly like this. Focus on making the output clear and readable.

---

# ⭐ Bonus Challenge

Add input validation.

The program should prevent users from entering a score below `0` or above `100`.

For example:

```text
Enter score for subject 1: 120

Invalid score!
Score must be between 0 and 100.
```

You may use a loop to continue asking until the user enters a valid score.

---

# 🧠 Concepts You Must Demonstrate

Your solution must demonstrate the following:

### Data Types

Use:

```python
str
int
float
list
```

### Conditions

Use:

```python
if
elif
else
```

### Loops

Use at least one:

```python
for
```

or

```python
while
```

### Lists

Use a list to store the five subject scores.

---

# 📂 Repository Structure

Organize your repository like this:

```text
python-student-result/
│
├── README.md
│
└── student_result_checker.py
```

---

# 🚫 Rules

1. Write the solution yourself.
2. Do not copy another student's solution.
3. Do not submit code you cannot explain.
4. Do not use advanced libraries or frameworks.
5. Keep the solution simple.
6. Your code should be readable.
7. Use meaningful variable names.
8. Test your program before submitting.

---

# 💡 After Completing the Assignment

You should be able to explain:

### 1. Data Types

* Why is the student's name a `string`?
* Why is age an `integer`?
* Why is the average capable of being a `float`?
* Why did you use a `list` for the scores?

### 2. Conditions

* Why did you use `if`, `elif`, and `else`?
* How does your program determine the grade?
* How does it determine whether the student passed?

### 3. Loops

* Why did you use a loop?
* What would happen if you had to collect scores for 100 subjects?
* What problem does the loop solve?

### 4. Your Code

Be prepared to explain **every major part of your program**.

---

# ✅ Submission

Before submitting, make sure:

* [ ] `student_result_checker.py` exists.
* [ ] The program runs without errors.
* [ ] Student information is collected.
* [ ] Five subject scores are collected using a loop.
* [ ] Scores are stored in a list.
* [ ] Total is calculated.
* [ ] Average is calculated.
* [ ] Grade is determined using conditions.
* [ ] Pass/Fail status is determined.
* [ ] Output is clear and readable.
* [ ] Code is pushed to your GitHub repository.

---

## 🎓 Final Goal

This assignment is not about writing a large amount of code.

The goal is to demonstrate that you understand how to take a **real-world problem** and break it down into:

```text
Data → Variables → Input → Loop → Calculation → Condition → Output
```

**Keep it simple. Understand your code. Be able to explain it.**
