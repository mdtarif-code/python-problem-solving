def second_largest_number(num):
    largest=num[0]
    second_largest=num[0]
    for i in num:
        if i>largest:
            second_largest = largest
            largest = i
        elif i>second_largest:
            second_largest = i

    return second_largest

numbers = [10, 25, 8, 40, 35]
result=second_largest_number(numbers)
print(result)
        



