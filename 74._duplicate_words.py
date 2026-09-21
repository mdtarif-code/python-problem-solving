def duplicate_words(text):
    words = text.split()
    seen = {}
    for word in words:
        if word in seen:
            seen[word] += 1
        else:
            seen[word] = 1

    duplicates = []
    for key,value in seen.items():
        if value > 1:
            duplicates.append(key)

    return duplicates

text = "python is easy and python is useful"
print(duplicate_words(text))