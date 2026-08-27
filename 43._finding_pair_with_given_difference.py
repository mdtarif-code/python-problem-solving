def is_pair_with_given_difference(numbers,k):

    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if abs(numbers[i]-numbers[j])==k:
                return True

    return False

numbers = [1, 7, 3, 9]
K = 5
result = is_pair_with_given_difference(numbers,K)
print(result)