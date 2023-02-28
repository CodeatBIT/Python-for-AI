# WAP which finds out whether a given name is present in a list or not.

# define a list of names
names = ["Abhishek", "Aashish", "Sapana", "Sanjana", "Sita"]

# take input from the user
name = input("Enter a name to search for: ")

# check if the name is present in the list
if name in names:
    print("Yes, the name is present in the list.")
else:
    print("No, the name is not present in the list.")
