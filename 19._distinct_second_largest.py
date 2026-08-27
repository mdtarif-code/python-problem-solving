def second_largest_distinct(num):
    largest = num[0]
    second_largest = num[0]
    for i in num:
        if i == largest:
                continue
        elif i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest:
            second_largest = i
    return second_largest

numbers = [10, 5, 8, 20, 15, 20]
result = second_largest_distinct(numbers)
print("The second largest number is:",result)