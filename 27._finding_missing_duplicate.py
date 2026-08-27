def find_duplicate(num):

    seen= []
    for i in num:
        if i not in seen:
            seen.append(i)
        else:
            return i


numbers = [1, 2, 3, 4, 5, 5]
result = find_duplicate(numbers)
print(result)