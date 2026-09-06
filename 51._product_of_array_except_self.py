# Given a list of integers, create a new list where each element 
# is the product of all the other elements except itself.

def product_of_array_except_itself(numbers):

    
    new_numbers = []
    left = 1
    for current in numbers:
        new_numbers.append(left)
        left *= current

    right = 1
    for i in range(len(numbers)-1, -1, -1):
        new_numbers[i] *= right
        right *= numbers[i]

    return new_numbers

numbers = [1, 2, 3, 4]
#numbers = [2, 3, 4]
result = product_of_array_except_itself(numbers)
print(result)