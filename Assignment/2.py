# WAP to find out weather a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

# take input from the user
sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))

# calculate total marks and percentage
total = sub1 + sub2 + sub3
percentage = (total / 300) * 100

# check if the student has passed or failed
if percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print("Congratulations, you have passed the exam!")
else:
    print("Sorry, you have failed the exam.")
