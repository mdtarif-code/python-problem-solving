def smallest_missing_positive(numbers):

    if not numbers or max(numbers)<1:
        return 1
    
    for i in range(1, max(numbers)+2):
        if i not in numbers:
            return i

numbers = []
result = smallest_missing_positive(numbers)
print(result)