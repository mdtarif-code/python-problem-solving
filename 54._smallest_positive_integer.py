def smallest_positive_int(numbers):
    seen = set(numbers)

    if 1 not in seen:
        return 1
       
    for i in range(1,max(numbers)+2):
        if i not in seen:
            return i

numbers = [-5, -2, 0]
result = smallest_positive_int(numbers)
print(result)