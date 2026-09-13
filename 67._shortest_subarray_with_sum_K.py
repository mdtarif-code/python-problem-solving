def shortest_subarray(numbers,k):
    seen = {0:-1}
    running_sum = 0
    shortest = float('inf')
    for i in range(len(numbers)):

        running_sum += numbers[i]
        pre_sum = running_sum-k
        if pre_sum in seen:
            shortest = min(shortest,(i-seen[pre_sum]))

        seen[running_sum] = i

    if shortest == float('inf'):
        return None
    else:
        return shortest

numbers = [2, 3, 1, 2, 4, 3]
k = 7
result = shortest_subarray(numbers,k)
print(result)