def pairs_with_sum_k(numbers,k):
    seen = set()
    result = set()
    for i in numbers:

        other = k - i
        if other in seen:
            result.add((other,i))

        seen.add(i)
        
    return list(result)


numbers = [1, 1, 2, 2, 3, 3]
K = 4
result = pairs_with_sum_k(numbers,K)
print(result)