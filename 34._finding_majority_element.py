def majority_element(numbers):

    frequecy = {}
    for i in numbers:
        if i in frequecy:
            frequecy[i] += 1
        else:
            frequecy[i] = 1

    for element , count in frequecy.items():
        if count>len(numbers)/2:
            return element
   
    return None

numbers = [1, 2, 3, 4]
result = majority_element(numbers)
print(result)