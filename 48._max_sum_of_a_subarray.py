def max_sum_of_a_subarray(numbers):
    largest = numbers[0]
    current_sum = numbers[0]
    for num in numbers[1:]:
        if num>current_sum+num:
            current_sum = num
        else:
            current_sum = num+current_sum

        if current_sum>largest:
            largest = current_sum

    return largest

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_sum_of_a_subarray(numbers)
print(result)