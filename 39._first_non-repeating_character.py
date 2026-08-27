def first_non_repeating(text):
    frequency = {}
    for i in text:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    for key,value in frequency.items():
        if value ==1:
            return key

    return None

text = "swiss"
result = first_non_repeating(text)
print(result)