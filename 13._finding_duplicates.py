def duplicates(num):
    seen = []
    duplicate =[]
    for i in num:
        if i not in seen:
            seen.append(i)
        elif i not in duplicate:
            duplicate.append(i)

    return duplicate

numbers = [10, 20, 30, 40]
result = duplicates(numbers)
print(result)