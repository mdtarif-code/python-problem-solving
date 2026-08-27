def most_frequent_character(str):

    new_str = [x for x in str if x != " "]
    frequency = {}
    for i in new_str:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    maxm = 0
    word = None
    for key, value in frequency.items():
        if value > maxm:
            maxm = value
            word = key

    return word



text = "data science"
result = most_frequent_character(text)
print(result)