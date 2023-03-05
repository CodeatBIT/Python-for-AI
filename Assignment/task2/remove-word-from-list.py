def remove_word_from_list(word, lst):
    new_list = []
    for item in lst:
        if item != word:
            new_list.append(item)
    return new_list


words = ["apple", "banana", "orange", "pear"]
new_words = remove_word_from_list("banana", words)
print(new_words)
