# A spam comment is defined as a text containing following keywords: "Make a lot of money", "Buy now", "Subscribe this", "Click this". WAP a program to detect these spam.

# take input from the user
comment = input("Enter your comment: ")

# define a list of spam keywords
spam_keywords = ["Make a lot of money", "Buy now", "Subscribe this", "Click this"]

# check if the comment contains any spam keywords
contains_spam = False
for keyword in spam_keywords:
    if keyword in comment:
        contains_spam = True
        break

# display the result
if contains_spam:
    print("Sorry, your comment contains spam.")
else:
    print("Your comment is valid.")
