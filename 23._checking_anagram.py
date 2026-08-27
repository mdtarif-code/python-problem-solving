def is_anagram(text1, text2):

    txt1 = text1.lower()
    txt2 = text2.lower()

    if len(txt1) != len(txt2):
        return False

    freq1 = {}
    freq2 = {}
    for i in txt1:
        if i in freq1:
            freq1[i] += 1
        else:
            freq1[i] = 1

    for i in txt2:
        if i in freq2:
            freq2[i] += 1
        else:
            freq2[i] = 1

    return freq1 == freq2


text1 = "Listen"
text2 = "silent"
result = is_anagram(text1, text2)
print(result)
