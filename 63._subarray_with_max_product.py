def subarray_with_max_product(numbers):
    pre = 1
    suff = 1
    maxx = -float('inf')
    for i in range(len(numbers)):
        if pre==0:
            pre = 1
        if suff==0:
            suff = 1

        pre = pre*numbers[i]
        suff = suff*numbers[len(numbers)-i-1]
        
        maxx = max(maxx, max(pre,suff))

    return maxx

numbers = [-2, 3, -4]
result = subarray_with_max_product(numbers)
print(result)