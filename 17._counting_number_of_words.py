def count_words(string):
    string_list = string.split()
    count = 0
    for word in string_list:
        count += 1

    return count

text = ""
result = count_words(text)
print(f"The total words are: {result}")