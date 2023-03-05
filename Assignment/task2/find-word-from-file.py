def check_file_for_word(filename, word):
    with open(filename, 'r') as file:
        for line in file:
            if word in line:
                return True
    return False


# filename = "twinkle.txt"
filename = "D:\\Workspace\\Python\\Assignment\\task2\\twinkle.txt"
word = "twinkle"

if check_file_for_word(filename, word):
    print(f"The file {filename} contains the word '{word}'.")
else:
    print(f"The file {filename} does not contain the word '{word}'.")
