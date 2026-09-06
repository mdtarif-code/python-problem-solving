def max_sum_of_two_elements(numbers):
    if len(numbers)<2:
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        if num>largest:
            second_largest = largest
            largest = num
        elif num>second_largest:
            second_largest = num

    return largest + second_largest

numbers = [-10, -3, -7, -2]
result = max_sum_of_two_elements(numbers)
print(result)