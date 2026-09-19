def shortest_word(text):

    words = text.split()
    lenn = float('inf')
    shortest = ""
    for word in words:
        if len(word)<lenn:
            shortest = word
            lenn = len(word)

    return shortest


text = "Data science is interesting"
result = shortest_word(text)
print(result)