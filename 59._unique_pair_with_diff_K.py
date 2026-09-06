def unique_pair_with_diff_K(numbers,k):
    new_numbers = set(numbers)
    result = set()
    for num in new_numbers:
        other = num+k
        if other in new_numbers:
            result.add((num,other))

    return result



numbers = [1, 5, 3, 4, 2]
K = 2
result = unique_pair_with_diff_K(numbers,K)
print(result)