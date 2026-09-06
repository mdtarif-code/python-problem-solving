def first_char_appears_once(text):

    frequency = {}
    for i in text:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    for char in text:
        if frequency[char] == 0:
            return char

    return None

#text = "aabbccdeef"
text = "aabbcc"
result = first_char_appears_once(text)
print(result)