def no_duplicates(numbers):
    new_list = []
    for i in numbers:
        if i not in new_list:
            new_list.append(i)
    return new_list

numbers = [1, 2, 3, 2, 4, 5, 3, 1]
result = no_duplicates(numbers)
print(result)