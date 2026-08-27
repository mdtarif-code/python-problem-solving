def second_most_frequent(numbers):
    frequency = {}
    for i in numbers:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    if len(frequency)<2:
        return None
    
    most = 0
    most_key = None
    second_most = 0
    second_most_key = None
    for key,value in frequency.items():
        if value>most:
            second_most = most
            second_most_key = most_key

            most = value
            most_key = key
        elif value>second_most:
            second_most = value
            second_most_key = key

    return second_most_key


numbers = [5, 5, 5,2]
result = second_most_frequent(numbers)
print(result)