def smallest_difference(num):

    smallest = float("inf")
    pair = []
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            diff = abs(num[i] - num[j])
            if diff<smallest:
                smallest = diff
                pair = [num[i], num[j]]


    return pair


numbers = [1, 5, 9, 12]
result = smallest_difference(numbers)
print(result)