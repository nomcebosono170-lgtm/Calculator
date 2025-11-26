def calculate_grade(average):
    if average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

print("----- STUDENT GRADER -----")

name = input("Enter student name: ")
subjects = int(input("How many subjects? "))

marks = []
for i in range(subjects):
    score = float(input(f"Enter mark for subject {i+1}: "))
    marks.append(score)

average = sum(marks) / len(marks)
grade = calculate_grade(average)

print("\n----- RESULTS -----")
print("Student:", name)
print("Average:", round(average, 2))
print("Final Grade:", grade)