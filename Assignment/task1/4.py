# WAP to find wheather a given user name contains less than ten characters or not.

# take input from the user
username = input("Enter your username: ")

# check the length of the username
if len(username) < 10:
    print("Your username contains less than ten characters.")
else:
    print("Your username contains ten or more characters.")
