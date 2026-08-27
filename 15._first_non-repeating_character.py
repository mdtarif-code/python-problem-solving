def first_non_repeating_character(string):
    dictionary = {}
    for i in string:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    for key, value in dictionary.items():
        if value == 1:
            return key


text = "swiss"
result = first_non_repeating_character(text)
print(result)
        
