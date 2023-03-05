# WAP to find the greatest of four numbers entered by the user.

# take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

# find the greatest number
max_num = num1
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3
if num4 > max_num:
    max_num = num4

# display the result
print("The greatest number is", max_num)
