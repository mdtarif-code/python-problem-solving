def missing_number(numbers):

    missing_num = []
    for i in range(1,max(numbers)+2):
        if i not in numbers:
            missing_num.append(i)
            return missing_num
    
         
numbers = [1, 2, 3, 4, 5, 6]
result = missing_number(numbers)
print(result)