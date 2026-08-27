def negative_numbers_at_first(number):
    negative_number = []
    non_negative_number = []

    for num in number:
        
        if num<0:
            negative_number.append(num)
        else:
            non_negative_number.append(num)

    return negative_number+non_negative_number

numbers = [1, -2, 3, -4, 5, -6]
result = negative_numbers_at_first(numbers)
print(result)