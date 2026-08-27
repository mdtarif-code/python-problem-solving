def removing_duplicates(text):
    seen = ""
    for i in text:
        if i not in seen:
            seen = seen+i

    return seen

text = "hello world"
result = removing_duplicates(text)
print(result)