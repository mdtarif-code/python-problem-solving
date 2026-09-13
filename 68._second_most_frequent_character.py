def second_most_frequent_character(text):
    frequency = {}
    for c in text:
        if c in frequency:
            frequency[c] += 1
        else:
            frequency[c] = 1

    maxx = 0
    second_maxx = 0
    for key,value in frequency.items():
        if value>maxx:
            second_maxx = maxx
            maxx = value
        elif value> second_maxx:
            second_maxx = value

    if maxx==second_maxx:
        return None

    for key, value in frequency.items():
        if value==second_maxx:
            return key

    return None

text = "aabbcc"
result = second_most_frequent_character(text)
print(result)