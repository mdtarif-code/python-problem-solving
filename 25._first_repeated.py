def first_repeated(lst):

    seen = []
    for i in lst:
        if i not in seen:
            seen.append(i)
        else:
            return i

    return None

numbers = [1, 2, 3, 4]
result = first_repeated(numbers)
print(result)