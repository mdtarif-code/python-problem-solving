def pair_with_sum(numbers,k):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):

            if numbers[i] + numbers[j] == k:
                return [numbers[i],numbers[j]]
    return None

numbers = [5,3,7]
k = 10

result = pair_with_sum(numbers,k)
print(result)