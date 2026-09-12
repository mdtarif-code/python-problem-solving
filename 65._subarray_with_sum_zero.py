def subarray_with_sum_zero(numbers):
    seen = {0}
    running_sum = 0
    for num in numbers:

        running_sum += num

        pre_sum = running_sum
        if pre_sum in seen:
            return True
        
        seen.add(running_sum)

    return False

#numbers = [4, 2, -3, 1, 6]
#numbers = [3, 4, -7, 5, -2, 1]
# numbers = [5, 3, 0, 7]
numbers = [5, 7, 3, -10]
result = subarray_with_sum_zero(numbers)
print(result)