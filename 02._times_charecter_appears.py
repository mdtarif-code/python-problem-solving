def times_caracter_appears(text):

    dic = {}
    for c in text:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1

    return dic
text = "banana"
result = times_caracter_appears(text)
print(result)