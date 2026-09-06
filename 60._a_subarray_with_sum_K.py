def subarray_with_sum_K(numbers,k):

    seen = {0}
    running_sum = 0
    for i in numbers:
        running_sum += i

        previous_sum = running_sum-k
        
        if previous_sum in seen:
            return True

        seen.add(running_sum)
        
    return False
        
numbers = [1, 4, 20, 3, 10, 5]
K = 33
result = subarray_with_sum_K(numbers,K)
print(result)
