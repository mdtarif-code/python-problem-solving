def subarray_with_min_product(numbers):
    pre = 1
    suff = 1
    minn = float('inf')
    for i in range(len(numbers)):
        if pre==0:
            pre = 1
        if suff==0:
            suff = 1

        pre *= numbers[i]
        suff *= numbers[len(numbers)-i-1]

        minn = min(minn, min(pre,suff))

    return minn

#numbers = [-2, 3, 0, -4, 5, -2]
numbers = [2, 3, -2, 4]
result = subarray_with_min_product(numbers)
print(result)