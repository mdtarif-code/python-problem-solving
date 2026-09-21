def compress_consecutive_repeated_char(text):
    curr = text[0]
    count = 0
    lst = [text[0]]
    for c in text:
        if c==curr:
            count += 1
        else:
            lst.append(count)
            lst.append(c)
            count = 1
            curr = c
    lst.append(count)

   
    return "".join(str(item) for item in lst)

text = "aabbbcdd"
result = compress_consecutive_repeated_char(text)
print(result)