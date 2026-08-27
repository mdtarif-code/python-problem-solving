def remove_duplicates(number):
    seen = []
    for i in number:
        if i not in seen:
            seen.append(i)

    return seen

numbers = [1, 2, 2, 3, 1, 4, 3]
result = remove_duplicates(numbers)
print(result)