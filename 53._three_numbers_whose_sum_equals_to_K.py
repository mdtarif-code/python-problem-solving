def three_numbers_sum_equals_to_k(numbers,k):

    for current in range(len(numbers)):
        others = k-numbers[current]

        seen_for_others = set()
        for second in numbers[current+1:]:
            third = others - second
            if third in seen_for_others:
                return True
            seen_for_others.add(second)

    return False

numbers = [1, 4, 6, 8, 10]
K = 15
result = three_numbers_sum_equals_to_k(numbers,K)
print(result)