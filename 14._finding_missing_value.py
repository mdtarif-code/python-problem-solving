def find_missing_value(num):
    missing = 0
    for i in range(len(num)+1):
        if i not in num:
            missing = i
            return missing

numbers = [0, 1]
result = find_missing_value(numbers)
print(result)