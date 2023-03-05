# WAP to calculate the grade of a student from his marks from the following scheme:
#   Marks               Grade
#   >= 90 and <=100     Excellent
#   >= 80 and < 90      A
#   >= 70 and < 80      B
#   >= 60 and < 70      C
#   >= 50 and < 60      D
#   < 50                F

# Take input from the user
marks = float(input("Enter your marks: "))

# Calculate the grade
if marks >= 90 and marks <= 100:
    grade = "Excellent"
elif marks >= 80 and marks < 90:
    grade = "A"
elif marks >= 70 and marks < 80:
    grade = "B"
elif marks >= 60 and marks < 70:
    grade = "C"
elif marks >= 50 and marks < 60:
    grade = "D"
else:
    grade = "F"

# Display the grade
print("Your grade is:", grade)
