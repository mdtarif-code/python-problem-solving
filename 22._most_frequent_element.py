def most_frequent_element(number):

    elements = {}
    for i in number:
        if i in elements:
            elements[i] += 1
        else:
            elements[i] = 1

    
    maxm = None
    max_count = 0
    for key, value in elements.items():
        if value>max_count:
            max_count = value
            maxm = key

    return maxm   


numbers = [1, 3, 2, 1, 4, 1, 3]
result = most_frequent_element(numbers)
print("The most frequent element is:",result)